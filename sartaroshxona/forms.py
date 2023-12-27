# forms.py
from django import forms
from .models import Service, Barber

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'  # Use all fields from the Service model

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields['barber'].widget = forms.HiddenInput()  # Hide the 'barber' field in the form

class BarberForm(forms.ModelForm):
    class Meta:
        model = Barber
        fields = '__all__'  # Use all fields from the Barber model

        
        
