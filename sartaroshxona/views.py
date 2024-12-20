# Sartaroshxona views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Barber, Service
from .forms import BarberForm, ServiceForm
from clients.forms import UserProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required
from main.decorators import is_barber_required
from django.contrib import messages
from django.urls import reverse


@login_required
@is_barber_required
def barber_profile(request):
    user = request.user
    barber = Barber.objects.get(user=user)  # Fetch the logged-in barber's data
    
    if request.method == 'POST':
        if 'user_info_form' in request.POST:
            user_form = UserProfileForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                return redirect('barber_profile')
            
        elif 'password_change_form' in request.POST:
            password_change_form = PasswordChangeForm(request.user, request.POST)
            if password_change_form.is_valid():
                user = password_change_form.save()
                update_session_auth_hash(request, user)
                return redirect('barber_profile')
            

        elif 'barber_info_form' in request.POST:
            barber = Barber.objects.get(user=user)
            old_profile_image = barber.profile_image  # Get the old profile image

            barber_form = BarberForm(request.POST, request.FILES, instance=barber)
            if barber_form.is_valid():
                # Check if a new image was uploaded and delete the old one
                if old_profile_image and 'profile_image' in request.FILES:
                    profile_image = request.FILES['profile_image']
                    if profile_image.size <= 500 * 1024:  # 500 KB in bytes
                        if os.path.isfile(os.path.join(settings.MEDIA_ROOT, str(old_profile_image))):
                            os.remove(os.path.join(settings.MEDIA_ROOT, str(old_profile_image)))
                    else:
                        messages.error(request, 'Изображение должно быть не более 500 КБ. Переформатируйте его с помощью ссылки "Изменить размер изображения" ниже или отправьте свою фотографию через Telegram и загрузите ее оттуда для автоматического изменения размера.')
                        return redirect(reverse('barber_profile'))
                    
                barber_form.save()
                return redirect('barber_profile')
        
        elif 'delete_image' in request.POST:
            barber = Barber.objects.get(user=request.user)
            old_profile_image = barber.profile_image

            if old_profile_image:  # Check if the image exists
                # Delete the image file
                barber.profile_image.delete()
                # Set profile_image field to null to clear the image field
                barber.profile_image = None
                barber.save()
                return redirect('barber_profile')

            
        elif 'service_edit_form' in request.POST:
            service_ids = request.POST.getlist('id[]')
            titles = request.POST.getlist('title[]')
            prices = request.POST.getlist('price[]')
            durations = request.POST.getlist('duration_minutes[]')
            print(service_ids)

            for i, service_id in enumerate(service_ids):
                service = Service.objects.get(pk=service_id)
                service.title = titles[i]
                service.price = prices[i]
                service.duration_minutes = durations[i]
                service.save()

            return redirect('barber_profile')
        
        elif 'service_delete_form' in request.POST:
            service_ids_to_delete = request.POST.getlist('delete[]')
            for service_id in service_ids_to_delete:
                service = Service.objects.get(pk=service_id)
                service.delete()

            return redirect('barber_profile')
        

        elif 'service_form' in request.POST:  # Add new service
            service_form = ServiceForm(request.POST)
            if service_form.is_valid():
                service = service_form.save(commit=False)
                service.master = barber  # Associate the service with the logged-in barber
                service.save()
                return redirect('barber_profile')
            
        elif 'active_barber' in request.POST:
            payment_fee_labels = {
                'Таджикистан': '30 TJS',
                }
            payment_fee = payment_fee_labels.get(str(user.country))

            if barber.payment:
                barber.active_barber = not barber.active_barber
                barber.save()
                return redirect('barber_profile')
            
            else:
                return render(request, 'main/others.html', {
                    'barber': barber,
                    'display': 'payment_info',
                    'payment_fee': payment_fee,
                    
                    })
            

        

    else:
        barber_form = BarberForm(instance=barber)
        service_initial = {'barber': barber}
        service_form = ServiceForm(initial=service_initial)
        user_form = UserProfileForm(instance=request.user)
        password_change_form = PasswordChangeForm(request.user)
        if barber.payment:
            payment_expiration_date_naive = barber.payment_expiration_date.replace(tzinfo=None)
            # Perform the subtraction operation
            print(barber.get_user_time_zone())
            left_days = (payment_expiration_date_naive - barber.get_user_time_zone()).days
            left_days = max(left_days, 0)  # Ensure left_days is non-negative
            if int(left_days) == 0:
                barber.deactivate_premium()
        else:
            left_days = 0

    services = barber.get_services()  # Fetch services associated with the current barber

    return render(request, 'sartaroshxona/prof.html', {
        'user_form': user_form,
        'password_change_form': password_change_form,
        'barber': barber,
        'barber_form': barber_form,
        'services': services,
        'service_form': service_form,
        'left_days': left_days

    })

#--------------------------All done above, don't  make changes--------------------

from clients.models import Appointment  # Import the Appointment model
from main.models import CustomUser
from .models import ClientBarberInteraction, DailyWorkRecord



@login_required
@is_barber_required
def appointments_by_category(request, category):
    status_choices = dict(Appointment.STATUS_CHOICES)
    category_labels = {
        'in_queue': 'В очереди',
        'confirmed': 'Подтверждено',
        'done': 'История',
        'money': 'Заработанные деньги'
        }
    human_readable_category = category_labels.get(category)

    logged_in_barber = request.user  # Assuming the logged-in user is the barber
    barber_model = Barber.objects.get(user=logged_in_barber)
    appointments = None
    appointment_in_queue = Appointment.objects.filter(barber__user=logged_in_barber, status='in_queue').prefetch_related('service')
    appointment_confirmed = Appointment.objects.filter(barber__user=logged_in_barber, status='confirmed').prefetch_related('service')
    interactions = ClientBarberInteraction.objects.filter(barber=barber_model)
    daily_work_records = DailyWorkRecord.objects.filter(barber=barber_model)

    if category == 'in_queue':
        appointments = appointment_in_queue.order_by('appointment_time')
    elif category == 'confirmed':
        appointments = appointment_confirmed.order_by('appointment_time')
    elif category == 'done':
        pass
    elif category == 'money':
        pass
    else:
       return render(request, 'main/404.html')

    # COUNT ITEMS FOR RENDERING BELOW HEADER
    appointment_in_queue_count = appointment_in_queue.count()
    appointment_confirmed_count = appointment_confirmed.count()
    interactions_count = interactions.count()
    daily_work_records_count = daily_work_records.count()

    # CONTENT FOR HTML


    # RETURN 
    return render(request, 'sartaroshxona/clients.html', {
        'appointments': appointments,
        'category': category,
        'human_readable_category': human_readable_category,
        'appointment_in_queue_count': appointment_in_queue_count,
        'appointment_confirmed_count': appointment_confirmed_count,
        'interactions_count': interactions_count,
        'daily_work_records_count': daily_work_records_count,
        'currency': barber_model.currency,
        'interactions': interactions,
        'daily_work_records': daily_work_records,
    })


from django.db.models import Sum
from datetime import date

@login_required
@is_barber_required
def accept_and_done_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.status = 'confirmed'  # Assuming you update status field to 'confirmed' when accepted
    appointment.save()
    # Redirect back to appointments page or any other page
    return redirect('appointments_by_category', category='in_queue')

def accept_and_done_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)

    if 'accept' in request.POST:
        # Change status to 'confirmed' if 'Accept' button is clicked
        appointment.status = 'confirmed'
        appointment.save()
        # Redirect back to appointments page or any other page
        return redirect('appointments_by_category', category='in_queue')
    
    elif 'done' in request.POST:
        
        # Increment times_appointed for the user
        client_id = appointment.client.id
        barber_id = appointment.barber.id
        client = get_object_or_404(CustomUser, id=client_id)
        barber = get_object_or_404(Barber, id=barber_id)
        # Get or create the ClientBarberInteraction instance
        interaction, created = ClientBarberInteraction.objects.get_or_create(client=client, barber=barber)

         # Increment times_appointed
        interaction.times_appointed += 1
        interaction.save()

        # Get the services associated with the appointment
        services = appointment.service.all()

        # Calculate the total price for the services
        total_price = services.aggregate(Sum('price'))['price__sum']

        # Get or create the DailyWorkRecord instance for the current date
        today = date.today()
        daily_work_record, created = DailyWorkRecord.objects.get_or_create(barber=barber, date=today)

        # Update the amount_worked in DailyWorkRecord
        daily_work_record.amount_worked += total_price
        daily_work_record.save()

        appointment.delete()


        return redirect('appointments_by_category', category='confirmed')

@login_required
@is_barber_required
def cancel_appointment(request, appointment_id, category):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.delete()  # Delete the appointment
    # Redirect back to appointments page or any other page
    return redirect('appointments_by_category', category=category)


#---------------------------------Work place above------------------------------


def client_or_barber(request):
    user = request.user
    user_in_barber_list = Barber.objects.filter(user=user).exists()
    if request.method == 'POST' and user_in_barber_list:
        user.is_barber = not user.is_barber
        user.save()
        # Redirect the user to the appropriate profile page
        if user.is_barber:
            return redirect('barber_profile')
        else:
            return redirect('client_profile')
    else:
        # Render the form for GET requests
        return render(request, 'main/404.html')


def test(request):
    return render(request, 'sartaroshxona/appointment.html')


