# Create your views here.

# views.py
from django.shortcuts import render, redirect
from clients.forms import UserProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def client_profile(request):
    user = request.user

    if request.method == 'POST':
        if 'user_info_form' in request.POST:
            user_form = UserProfileForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                return redirect('client_profile')
            
        elif 'password_change_form' in request.POST:
            password_change_form = PasswordChangeForm(request.user, request.POST)
            if password_change_form.is_valid():
                user = password_change_form.save()
                update_session_auth_hash(request, user)
                return redirect('client_profile')
            

    else:
        user_form = UserProfileForm(instance=request.user)
        password_change_form = PasswordChangeForm(request.user)


    return render(request, 'clients/client_profile.html', {
        'user_form': user_form,
        'password_change_form': password_change_form,
    })

