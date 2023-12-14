from django.shortcuts import render

def appointment(request):
    return render(request, 'sartaroshxona/appointment.html')

def sign(request):
    return render(request, 'sartaroshxona/sign.html')

def test(request):
    return render(request, 'sartaroshxona/profile.html')