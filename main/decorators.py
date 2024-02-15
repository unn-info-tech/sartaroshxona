from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect


def is_barber_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_barber:
            # User is authenticated and has is_barber set to True
            return view_func(request, *args, **kwargs)
        else:
            # User doesn't meet the requirements, return a forbidden response
            return render(request, 'main/404.html', {'error_message': 'Для доступа к этому URL требуется статус парикмахера'})

    return _wrapped_view

def is_client_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_barber:
            # User is authenticated and has is_barber set to True
            return view_func(request, *args, **kwargs)
        else:
            # User doesn't meet the requirements, return a forbidden response
            return render(request, 'main/404.html', {'error_message': 'Для доступа к этому URL требуется статус клиента'})

    return _wrapped_view
