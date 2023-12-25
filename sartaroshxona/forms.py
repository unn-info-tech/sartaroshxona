# forms.py
from django import forms
from .models import Service, Barber

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'  # Use all fields from the Service model

class BarberForm(forms.ModelForm):
    class Meta:
        model = Barber
        fields = '__all__'  # Use all fields from the Barber model
