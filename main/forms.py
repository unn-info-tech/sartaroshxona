from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_barber']  # Include the fields you want in the form

        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'is_barber': 'Barber',  # Customize labels for other fields if needed
        }
        
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter yor username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Ente your password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
            'is_barber': forms.CheckboxInput(attrs={'id': 'is_barber'}),
            # Add other fields' placeholders as needed
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'})

    def clean_username(self):
        username = self.cleaned_data['username']
        existing_user = CustomUser.objects.filter(username__iexact=username).exists()

        # Validate username format: allow letters, numbers, periods, and underscores
        if not username.replace('.', '').replace('_', '').isalnum():
            raise forms.ValidationError(
                'Enter a valid username. This value may contain only letters, numbers, periods, and underscores.'
            )

        # Check if the username already exists
        if existing_user:
            raise forms.ValidationError('This username is already taken.')

        return username.lower()  # Ensure username is lowercase

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username'].lower()  # Ensure username is lowercase
        if commit:
            user.save()
        return user

    

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


        