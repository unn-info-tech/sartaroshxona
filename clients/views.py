# Clients views.py
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, get_object_or_404
from clients.forms import UserProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from sartaroshxona.models import Barber, Service
from .forms import AppointmentForm
from .models import Appointment
import json
from django.contrib import messages
from django.urls import reverse
import datetime
from django.utils import timezone
import pytz
from .utils import is_overlapping
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from main.decorators import is_client_required
from sartaroshxona.models import ClientBarberInteraction

@login_required
@is_client_required
def client_profile(request):
    user = request.user

    if request.method == 'POST':
        if 'user_info_form' in request.POST:
            user_form = UserProfileForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                return redirect('client_profile')
            
        elif 'password_change_form' in request.POST:
            password_change_form = PasswordChangeForm(request.user, request.POST)
            if password_change_form.is_valid():
                user = password_change_form.save()
                update_session_auth_hash(request, user)
                return redirect('client_profile')
            

    else:
        user_form = UserProfileForm(instance=request.user)
        password_change_form = PasswordChangeForm(request.user)
        user_in_barber_list = Barber.objects.filter(user=user).exists()


    return render(request, 'clients/client_profile.html', {
        'user_form': user_form,
        'password_change_form': password_change_form,
        'user_in_barber_list': user_in_barber_list,

    })







from django.db.models import Q

@login_required
@is_client_required
def barbers_list(request):
    user = request.user

    country = user.country
    region = user.region
    district = user.district
    city = user.city

    # Use Q objects to construct the AND conditions for filtering
    q_filter = (
        Q(user__country=country) &
        Q(user__region=region) &
        Q(user__district=district) &
        Q(user__city=city)
    )

   # Filter barbers based on the user's address
    barbers = Barber.objects.filter(q_filter, active_barber=True)

    # Search functionality
    query = request.GET.get('query')
    if query:
        barbers = barbers.filter(Q(user__username__icontains=query))
        if not barbers.exists():  # If no barbers matched the query
            barbers = Barber.objects.filter(q_filter, active_barber=True)  # Retrieve all barbers

    return render(request, 'clients/barbers_list.html', {'header': "Список парикмахеров", 'barbers': barbers})


@login_required
@is_client_required
def favorites(request):
    user = request.user
    favorite_barbers = user.favorite_barbers.all()
    return render(request, 'clients/barbers_list.html', {'header': "Мои любимые парикмахеры", 'barbers': favorite_barbers})


@login_required
@is_client_required
def my_appointments(request, category):
    client = request.user
    interactions = ClientBarberInteraction.objects.filter(client=client)
    interactions_count = interactions.count()
    my_appointments = Appointment.objects.filter(client=client).prefetch_related('service')
    my_appointments_count = my_appointments.count()
    category_labels = {
        'my_appointments': 'Мои записи',
        'done': 'История',
        }
    human_readable_category = category_labels.get(category)

    return render(request, 'clients/my_appointments.html', {
        'my_appointments': my_appointments.order_by('appointment_time'),
        'interactions': interactions,
        'interactions_count': interactions_count,
        'my_appointments_count': my_appointments_count,
        'human_readable_category': human_readable_category,
        'category': category,
        })



@login_required
@is_client_required
def appointment(request, barber_id):
    barber = get_object_or_404(Barber, id=barber_id)
    services = Service.objects.filter(barber=barber)
    appointments = Appointment.objects.filter(barber=barber).order_by('appointment_time')

    if request.method == 'POST':
        if barber.user == request.user:
            messages.error(request, 'Вы не можете записаться на прием к самому себе')
            return redirect(reverse('appointment', args=[barber_id]))
        
        # Получение выбранных идентификаторов услуг из данных POST
        selected_service_ids_json = request.POST.get('selected_services')
        # Десериализация строки JSON в список Python
        selected_service_ids = json.loads(selected_service_ids_json)
        selected_services = Service.objects.filter(pk__in=selected_service_ids)
        appointment_form = AppointmentForm(request.POST)

        if selected_services and appointment_form.is_valid():
            total_duration = int(request.POST.get('total_duration'))
            appointment_time = appointment_form.cleaned_data['appointment_time']
            duration = datetime.timedelta(minutes=total_duration)
            end_time = appointment_time + duration

            now = barber.get_user_time_zone()
            appointment_time_naive = appointment_time.replace(tzinfo=None)
            
            if now <= appointment_time_naive: 

                if not is_overlapping(appointment_time, end_time):
                    appointment = appointment_form.save(commit=False)
                    appointment.barber = Barber.objects.get(id=barber_id)
                    appointment.client = request.user
                    appointment.appointment_end_time = end_time
                    
                    appointment.save()
                    appointment.service.add(*selected_services)

                    messages.success(request, 'Поздравляем, ваша запись создана')
                    return redirect(reverse('appointment', args=[barber_id]))
                else:
                    messages.error(request, 'Дата и время уже выбраны')
                    return redirect(reverse('appointment', args=[barber_id]))
            else:
                messages.error(request, 'Вы не можете записаться на прием в прошлом')
                return redirect(reverse('appointment', args=[barber_id]))

        else:
            messages.error(request, 'Дата и время или услуга не выбраны')
            return redirect(reverse('appointment', args=[barber_id]))

    else:
        appointment_form = AppointmentForm()

    return render(request, 'clients/appointment.html', {
        'barber': barber,
        'services': services,
        'appointments': appointments,
        'appointment_form': appointment_form,
    })






@login_required
@is_client_required
def update_favorites(request, barber_id):
    barber = Barber.objects.get(pk=barber_id)
    user = request.user

    if request.method == 'POST':
        if 'favorite' in request.POST:
            user.favorite_barbers.add(barber)
            messages.success(request, f'{barber.user.username} добавлен в избранное.')

        elif 'unfavorite' in request.POST:
            user.favorite_barbers.remove(barber)
            messages.success(request, f'{barber.user.username} удален из избранного.')


        print(user, user.favorite_barbers.all())
        return redirect(reverse('appointment', args=[barber_id]))  # Replace with the appropriate view name or URL pattern



   

    return render(request, 'clients/appointment.html')



