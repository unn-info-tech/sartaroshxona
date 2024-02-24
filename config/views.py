from django.shortcuts import redirect, render
from sartaroshxona.models import Barber
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ValidationError
from django.http import HttpResponseBadRequest, HttpResponse
from uuid import UUID

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def public_barbers(request):
    if request.method == 'POST':
        barber_ids_str = request.POST.get('barber_ids', '')
        barber_ids = barber_ids_str.split(',')
        error_ids = []
        activated_ids = []

        for barber_id in barber_ids:
            try:
                barber_id = barber_id.strip()
                uuid = UUID(barber_id)
            except ValueError:
                error_ids.append(barber_id)
                continue

            try:
                barber = Barber.objects.get(id=uuid)
                barber.payment = True
                barber.save()
                activated_ids.append(barber_id)
            except Barber.DoesNotExist:
                error_ids.append(barber_id)

        if error_ids:
            error_message = f"The following IDs are not valid or do not exist: {', '.join(error_ids)}"
            if activated_ids:
                error_message += f". Successfully activated IDs: {', '.join(activated_ids)}"
            return HttpResponseBadRequest(error_message)

        return HttpResponse("Barbers activated successfully!")

    return render(request, 'main/public_barber.html')
