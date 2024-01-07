from django import forms
from main.models import CustomUser
from .models import Appointment

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']  # Include fields that you want users to edit



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_time']
        widgets = {
            'appointment_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
