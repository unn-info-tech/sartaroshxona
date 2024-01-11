from django.contrib import admin
from .models import Barber, Service, ClientBarberInteraction
# Register your models here.

admin.site.register(Barber)
admin.site.register(Service)
admin.site.register(ClientBarberInteraction)

