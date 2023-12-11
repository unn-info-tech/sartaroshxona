from django.shortcuts import render

def appointment(request):
    return render(request, 'sartaroshxona/appointment.html')

def sign(request):
    return render(request, 'sartaroshxona/test.html')

def test(request):
    return render(request, 'sartaroshxona/test1.html')