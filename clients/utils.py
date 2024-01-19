from .models import Appointment
from django.utils import timezone

def is_overlapping(start_time, end_time):
    existing_appointments = Appointment.objects.filter(
        appointment_time__lt=end_time,
        appointment_end_time__gt=start_time,
    )

    return existing_appointments.exists()