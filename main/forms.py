from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'is_barber']  # Include the fields you want in the form

        labels = {
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'is_barber': 'Barber',  # Customize labels for other fields if needed
        }
        
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


from django.contrib.auth.forms import AuthenticationForm
from django.forms import TextInput, PasswordInput

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={'placeholder': 'Enter your username'})
        self.fields['password'].widget = PasswordInput(attrs={'placeholder': 'Enter your password'})

    class Meta:
        model = CustomUser  # Replace CustomUser with your user model
        fields = ['username', 'password']  # Fields present in the login form


        