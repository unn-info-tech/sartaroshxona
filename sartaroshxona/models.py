from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class WorkingTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='working_time')
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    launch_start_time = models.TimeField()
    launch_end_time = models.TimeField()
    price = models.CharField(max_length=10)

    def __str__(self) -> str:
        return str(self.date)
    
    
"""class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    # Other appointment details...

    def clean(self):
        working_time = self.user.working_time

        if not working_time:
            raise ValidationError("Working time not set for this user")

        if self.appointment_time.weekday() + 1 != working_time.day_of_week:
            raise ValidationError("Appointment on the wrong day")

        if (self.appointment_time.time() < working_time.start_time or
                self.appointment_time.time() >= working_time.end_time or
                (self.appointment_time.time() >= working_time.launch_start_time and
                 self.appointment_time.time() < working_time.launch_end_time)):
            raise ValidationError("Appointment time is not within working hours or during a break")
"""
