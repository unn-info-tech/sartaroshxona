from django.shortcuts import redirect

def middleware(request):
    if request.user.is_authenticated:
        if request.user.is_barber:  # Assuming is_barber is a boolean field in your User model
            return redirect('barber_profile')  # Redirect to the barber profile URL
        else:
            return redirect('client_profile')
    else:
        return redirect('signin')  # Redirect to login page if user is not logged in
