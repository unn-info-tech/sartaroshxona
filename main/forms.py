from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'is_barber']  # Include the fields you want in the form
        
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter yor username'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Ente your password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
            # Add other fields' placeholders as needed
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password from numbers and letters of the Latin alphabet'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'})