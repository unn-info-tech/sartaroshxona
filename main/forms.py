from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.forms import TextInput, PasswordInput
from .models import Country, City, Region, District




class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_barber', 'agreement', 'country', 'region', 'district', 'city']

        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'is_barber': 'Barber',
            # Customize labels for other fields if needed
        }

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Имя пользователя с малой буквы'}),
            'email': forms.TextInput(attrs={'placeholder': 'Электронная почта'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтверждение пароля'}),
            'is_barber': forms.CheckboxInput(attrs={'id': 'is_barber'}),
            # Добавьте необходимые подсказки для других полей
        }


    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label="Выберите страну")
    
    region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label="Выберите регион")

    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label="Выберите район")

    city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="Выберите город")


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтверждение пароля'})

        

        


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


class CustomAuthenticationForm(AuthenticationForm):
    

    class Meta:
        model = CustomUser  # Replace CustomUser with your user model
        fields = ['username', 'password']  # Fields present in the login form


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={'placeholder': 'Имя пользователя с малой буквы'})
        self.fields['password'].widget = PasswordInput(attrs={'placeholder': 'Введите ваш пароль'})




