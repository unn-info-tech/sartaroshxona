from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.http import HttpResponse
from .models import CustomUser

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import CustomUser  # Import your CustomUser model

'''from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        formMe_signup = UserCreationForm(request.POST)  # Create a form instance and populate it with data from the request
        if formMe_signup.is_valid():  # Check if the form data is valid
            user = formMe_signup.save()  # Save the user to the database
            # Log the user in after successful signup
            username = formMe_signup.cleaned_data.get('username')  # Get the username from the form data
            raw_password = formMe_signup.cleaned_data.get('password1')  # Get the password from the form data
            user = authenticate(username=username, password=raw_password)  # Authenticate the user
            login(request, user)  # Log the user in
            # Redirect to a different page after successful signup and login
            return redirect('home')  # Replace 'home' with your desired URL name or path
    else:
        formMe_signup = UserCreationForm()  # If it's a GET request, create a blank form

    return render(request, 'main/sign.html', {'formMe_signup': formMe_signup})  # Render the signup form template with the form instance'''




from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError  

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        formMe_signup = CustomUserCreationForm(request.POST)
        if formMe_signup.is_valid():
            user = formMe_signup.save()
            username = formMe_signup.cleaned_data.get('username')
            messages.success(request, f'Welcome, {username}! Your account has been created.')
    else:
        formMe_signup = CustomUserCreationForm()
    return render(request, 'main/signUp.html', {'formMe_signup': formMe_signup})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm

def signin(request):
    if request.method == 'POST':
        formMe_signIn = CustomAuthenticationForm(data=request.POST)
        if formMe_signIn.is_valid():
            username = formMe_signIn.cleaned_data.get('username')
            password = formMe_signIn.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
    else:
        formMe_signIn = CustomAuthenticationForm()
    return render(request, 'main/signIn.html', {'formMe_signIn': formMe_signIn})



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


'''def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('home')  # Redirect to your desired URL after successful login
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')  # Redirect to your desired URL after logout

@login_required
@require_POST
def delete_profile(request):
    if request.user.is_authenticated:
        user = request.user
        user.delete()
        messages.success(request, 'Profile deleted successfully!')
        return redirect('home')  # Redirect to your desired URL after profile deletion
    else:
        messages.error(request, 'You need to be logged in to delete your profile.')
        return redirect('login')  # Redirect to login if not authenticated
'''