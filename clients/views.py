# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from main.models import CustomUser

def user_profile(request):
    user = request.user
    user_form = UserProfileForm(instance=user)

    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('user_profile')

    return render(request, 'clients/user_profile.html', {
        'user_form': user_form
    })
