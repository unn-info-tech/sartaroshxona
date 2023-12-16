from django.shortcuts import redirect

class UserTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            if user.is_master:
                return redirect('sartaroshxona:barber_profile')  # Redirect to 'master_profile' URL in 'master' app
            else:
                return redirect('clients:client_profile')  # Redirect to 'client_profile' URL in 'client' app

        response = self.get_response(request)
        return response
