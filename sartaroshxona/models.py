from django.db import models
from main.models import CustomUser  # Assuming this is your CustomUser model

class Service(models.Model):
    barber = models.ForeignKey('Barber', on_delete=models.CASCADE, related_name='provided_services')
    title = models.CharField(max_length=50)
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('RUB', 'Russian Ruble'),
        ('TJS', 'Tajik Somoni'),
        ('UZS', 'Uzbekistani Soʻm'),
        # Add more currency choices here
    ]
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='TJS')
    duration_minutes = models.PositiveIntegerField()

    def __str__(self):
        return str(self.title)


class Barber(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='barber_profile')
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True, default='profile_images/default.png')
    phone_number = models.CharField(max_length=20, null=True, blank=True, default="")
    start_work = models.TimeField(null=True, blank=True)
    end_work = models.TimeField(null=True, blank=True)
    launch_start_time = models.TimeField(null=True, blank=True)
    launch_end_time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True,default="")
    my_clients = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='my_clients', null=True, blank=True)
   

    def get_services(self):
        return self.provided_services.all()  # Renamed related name for clarity

    def __str__(self):
        return str(self.user)
