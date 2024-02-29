from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages
from .models import CustomUser, Ads  # Import your CustomUser model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError  
from sartaroshxona.models import Barber
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from .utils import middleware

def signup(request):
    if request.method == 'POST':
        formMe_signup = CustomUserCreationForm(request.POST)
        if formMe_signup.is_valid():
            user = formMe_signup.save()

            username = formMe_signup.cleaned_data.get('username')
            messages.success(request, f'Добро пожаловать, {username}! Ваш аккаунт был успешно создан. Теперь выполните вход')


            # Check if the user is a barber and create a barber instance
            if user.is_barber:
                # Creating a Barber object with required fields
                barber = Barber.objects.create(
                    user=user,
                )
                barber.activate_premium(11)
            return redirect('signin')
    else:
        formMe_signup = CustomUserCreationForm()
    return render(request, 'main/signUp.html', {'formMe_signup': formMe_signup})




def signin(request):
    if request.method == 'POST':
        formMe_signIn = CustomAuthenticationForm(data=request.POST)
        if formMe_signIn.is_valid():
            username = formMe_signIn.cleaned_data.get('username')
            password = formMe_signIn.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return middleware(request)
                
    else:
        formMe_signIn = CustomAuthenticationForm()
    return render(request, 'main/signIn.html', {'formMe_signIn': formMe_signIn})


@login_required
def log_out(request):
    logout(request)
    return redirect('signin')  


@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('signin')  






#-----------------------------------Ads------------------------------------------------
    
from django.db.models import Q  # Import the Q object

def ads_list(request):
    user = request.user

    country = user.country
    region = user.region
    district = user.district
    city = user.city

    # Use Q objects to construct the AND conditions for filtering
    q_filter = (
        Q(ad_country=country) &  # Apply filter condition for country
        Q(ad_region=region) &    # Apply filter condition for region
        Q(ad_district=district) &  # Apply filter condition for district
        Q(ad_city=city)          # Apply filter condition for city
    )

    ads = Ads.objects.filter(q_filter)  # Use filter() instead of all()
    return render(request, 'main/ads.html', {'ads': ads})

@login_required
def others(request):
    return render(request, 'main/others.html', {'display': 'others',})


def tospp(request):
    return render(request, 'main/others.html', {'display': 'tospp',})

@login_required
def contact_dev(request):
    return render(request, 'main/others.html', {'display': 'contact_dev',})


@login_required
def feedback(request):
    return render(request, 'main/404.html', {'error_message': 'Страница еще не готова'})









'''def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print('afffffffffffffffffffff0', username)
        
        # Check for empty fields
        if not username or not password1 or not password2:
            messages.error(request, 'Please fill in all fields.')
            return redirect('signup')
        
        # Check if passwords match
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')
        

        
        # Check if the username already exists
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup')

        try:
            validate_password(password1, user=None)  # Pass 'user=None' for signup
        except ValidationError as error:
            messages.error(request, list(error.messages)[0])  # Display the first error message
            return redirect('signup')  # Redirect back to the signup page with error message

        # Create the user
        user = CustomUser.objects.create_user(username=username, password=password1)
        user.save()
        messages.success(request, f'Welcome, {username}! Your account has been created.')
        return HttpResponse("cool")
    else:
        return render(request, 'main/sign1.html')
'''