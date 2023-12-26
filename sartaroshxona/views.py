from django.shortcuts import render

def appointment(request):
    return render(request, 'sartaroshxona/appointment.html')

def sign(request):
    return render(request, 'sartaroshxona/sign.html')

def test(request):
    return render(request, 'sartaroshxona/clients.html')

# views.py
from django.shortcuts import render, redirect
from .models import Barber, Service
from .forms import BarberForm, ServiceForm

def barber_profile(request):
    barber = Barber.objects.get(user=request.user)  # Fetch the logged-in barber's data

    if request.method == 'POST':
        if 'barber_info_form' in request.POST:  # Update barber information
            barber_form = BarberForm(request.POST, request.FILES, instance=barber)
            if barber_form.is_valid():
                barber_form.save()
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
        service_form = ServiceForm()

    services = barber.get_services()  # Fetch services associated with the barber

    return render(request, 'sartaroshxona/prof.html', {
        'barber': barber,
        'barber_form': barber_form,
        'services': services,
        'service_form': service_form
    })
