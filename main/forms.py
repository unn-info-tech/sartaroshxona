from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.forms import TextInput, PasswordInput
from .models import Country, City, Region, District


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_barber', 'country', 'region', 'district', 'city']  # Include the fields you want in the form

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

    # FOR LOCATIONS:
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label="Select Country")

    region = forms.ModelChoiceField(queryset=Region.objects.none(), required=False,
                                    label="Region/State/Province")
    
    district = forms.ModelChoiceField(queryset=District.objects.none(), required=False,
                                    label="District/County")

    city = forms.ModelChoiceField(queryset=City.objects.none(), required=False,
                                    label="City/Town/Village")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].queryset = Region.objects.none()
        self.fields['district'].queryset = District.objects.none()
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['region'].queryset = Region.objects.filter(country_id=country_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['region'].queryset = self.instance.country.region_set.order_by('name')

        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['district'].queryset = District.objects.filter(region_id=region_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.region.district_set.order_by('name')

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['city'].queryset = City.objects.filter(district_id=district_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty queryset

        
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.district.city_set.order_by('name')


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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={'placeholder': 'Enter your username'})
        self.fields['password'].widget = PasswordInput(attrs={'placeholder': 'Enter your password'})

    class Meta:
        model = CustomUser  # Replace CustomUser with your user model
        fields = ['username', 'password']  # Fields present in the login form








