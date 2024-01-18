# Clients views.py
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from clients.forms import UserProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from sartaroshxona.models import Barber, Service
from .forms import AppointmentForm
from .models import Appointment
import json
from django.contrib import messages
from django.urls import reverse

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


    return render(request, 'clients/client_profile.html', {
        'user_form': user_form,
        'password_change_form': password_change_form,
    })




def barbers_list(request):
    barbers = Barber.objects.all()
    return render(request, 'clients/barbers_list.html', {'barbers': barbers})

#from .utils import is_overlapping

def appointment(request, barber_id):
    barber = Barber.objects.get(pk=barber_id)
    services = Service.objects.filter(barber=barber)

    if request.method == 'POST':
        # Retrieve the selected services IDs from the POST data
        selected_service_ids_json = request.POST.get('selected_services')
        # Deserialize the JSON string to a Python list
        selected_service_ids = json.loads(selected_service_ids_json)
        selected_services = Service.objects.filter(pk__in=selected_service_ids)
        appointment_form = AppointmentForm(request.POST)
        total_duration = request.POST.get('total_duration')
        print('========================================================', total_duration)

        if selected_services and appointment_form.is_valid():
            total_duration = request.POST.get('total_duration')
            print('========================================================',total_duration)


            appointment = appointment_form.save(commit=False)
            appointment.barber = Barber.objects.get(pk=barber_id)
            appointment.client = request.user
            
            appointment.save()
            appointment.service.add(*selected_services)

            messages.error(request, 'Congrats, your appoinment is done')
            return redirect(reverse('appointment', args=[barber_id]))

        else:
            # If no service is selected or form is invalid, redirect with an error message
           messages.error(request, 'Дата и время или служба не выбрана')
           return redirect(reverse('appointment', args=[barber_id]))

    else:
        appointment_form = AppointmentForm()

    return render(request, 'clients/appointment.html', {
        'barber': barber,
        'services': services,
        'appointment_form': appointment_form
    })


