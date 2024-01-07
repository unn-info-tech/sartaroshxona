# Sartaroshxona views.py
from django.shortcuts import render, redirect
from .models import Barber, Service
from .forms import BarberForm, ServiceForm
from clients.forms import UserProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
import os

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
                    if os.path.isfile(os.path.join(settings.MEDIA_ROOT, str(old_profile_image))):
                        os.remove(os.path.join(settings.MEDIA_ROOT, str(old_profile_image)))
                    
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
            currencies = request.POST.getlist('currency[]')
            durations = request.POST.getlist('duration_minutes[]')
            print(service_ids)

            for i, service_id in enumerate(service_ids):
                service = Service.objects.get(pk=service_id)
                service.title = titles[i]
                service.price = prices[i]
                service.currency = currencies[i]
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

    else:
        barber_form = BarberForm(instance=barber)
        service_initial = {'barber': barber}
        service_form = ServiceForm(initial=service_initial)
        user_form = UserProfileForm(instance=request.user)
        password_change_form = PasswordChangeForm(request.user)

    services = barber.get_services()  # Fetch services associated with the barber

    return render(request, 'sartaroshxona/prof.html', {
        'user_form': user_form,
        'password_change_form': password_change_form,
        'barber': barber,
        'barber_form': barber_form,
        'services': services,
        'service_form': service_form
    })


from django.shortcuts import render
from clients.models import Appointment  # Import the Appointment model

def barber_appointments(request):
    logged_in_barber = request.user  # Assuming the logged-in user is the barber

    # Fetch appointments related to the logged-in barber along with associated services
    appointments = Appointment.objects.filter(barber__user=logged_in_barber).prefetch_related('service')

    return render(request, 'sartaroshxona/client_test.html', {'appointments': appointments})




from django.shortcuts import get_object_or_404, redirect

def confirm_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Update the appointment confirmation status
    appointment.is_confirmed = True
    appointment.save()

    return redirect('barber_appointments')


def test(request):
    return render(request, 'sartaroshxona/appointment.html')
