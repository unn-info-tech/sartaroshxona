from django.shortcuts import redirect

def middleware(request):
    if request.user.is_authenticated:
        if request.user.is_barber:  # Assuming is_barber is a boolean field in your User model
            return redirect('appointments_by_category', category='in_queue')  # Redirect to the barber profile URL
        else:
            return redirect('barbers_list')
    else:
        return redirect('signin')  # Redirect to login page if user is not logged in
