from django.db import models
from main.models import CustomUser  # Import the CustomUser model from the 'main' app
from sartaroshxona.models import Barber, Service

class Appointment(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='client_appointments')
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name='barber_appointments')
    service = models.ManyToManyField(Service)  # Many-to-Many relationship with Service model
    appointment_time = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    
    # Add more fields as needed for your appointment details

    def __str__(self):
        return f"Appointment for {self.client.username} with {self.barber.user.username} at {self.appointment_time}"
