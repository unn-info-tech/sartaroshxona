from .models import Appointment

def is_overlapping(start_time, end_time):
    existing_appointments = Appointment.objects.filter(
        start_time__lt=end_time,
        end_time__gt=start_time
    )

    return existing_appointments.exists()