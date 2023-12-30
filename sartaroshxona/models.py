from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from main.models import CustomUser



class Service(models.Model):


    barber = models.ForeignKey('Barber', on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=50)
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('RUB', 'Russian Ruble'),
        ('TJS', 'Tajik Somoni'),
        ('UZS', 'Uzbekistani Soʻm'),  # Adding Uzbekistan's currency
        # Add more currency choices here
    ]
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price for the service
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='TJS')
    duration_minutes = models.PositiveIntegerField()  # Duration of the service in minutes

class Barber(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='working_time')
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    start_work = models.TimeField(null=True, blank=True)
    end_work = models.TimeField(null=True, blank=True)
    launch_start_time = models.TimeField(null=True, blank=True)
    launch_end_time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)

    # A method to get all services associated with a Master
    def get_services(self):
        return self.services.all()
    
    def __str__(self):
        return str(self.user)
