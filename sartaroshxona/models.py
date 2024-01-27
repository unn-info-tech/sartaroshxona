from django.db import models
from main.models import CustomUser  # Assuming this is your CustomUser model
from django.utils import timezone
import pytz
from datetime import timedelta

class Service(models.Model):
    barber = models.ForeignKey('Barber', on_delete=models.CASCADE, related_name='provided_services')
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_minutes = models.PositiveIntegerField()

    def __str__(self):
        return str(self.title)


class Barber(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='barber_profile')
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    start_work = models.TimeField(null=True, blank=True)
    end_work = models.TimeField(null=True, blank=True)
    launch_start_time = models.TimeField(null=True, blank=True)
    launch_end_time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True,default="")
    organization_name = models.CharField(max_length=50, null=True, blank=True,default="")

    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('RUB', 'Russian Ruble'),
        ('TJS', 'Tajik Somoni'),
        ('UZS', 'Uzbekistani Soʻm'),
        # Add more currency choices here
    ]
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='TJS')

   
   

    def get_services(self):
        return self.provided_services.all()  # Renamed related name for clarity
    
    def get_user_time_zone(self):
        if self.user.country and self.user.country.name == 'Russia':
            return (timezone.now().astimezone(pytz.timezone('Europe/Moscow')) - timedelta(minutes=1)).replace(tzinfo=None)
        elif self.user.country and self.user.country.name == 'Tajikistan':
            return (timezone.now().astimezone(pytz.timezone('Asia/Dushanbe')) - timedelta(minutes=1)).replace(tzinfo=None)
        else:
            # Default time zone or handle other countries as needed
             return (timezone.now() - timedelta(minutes=1)).replace(tzinfo=None)
        
    
    
    

    def __str__(self):
        return str(self.user)


class ClientBarberInteraction(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    times_appointed = models.PositiveIntegerField(default=0)


class DailyWorkRecord(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name='daily_work_records')
    date = models.DateField()
    amount_worked = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.barber.user.username} - {self.date} - Amount: {self.amount_worked}"