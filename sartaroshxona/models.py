from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):


    master = models.ForeignKey('Master', on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=50)
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

class Master(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='working_time')

    start_work = models.TimeField()
    end_work = models.TimeField()
    launch_start_time = models.TimeField()
    launch_end_time = models.TimeField()
    location = models.CharField(max_length=50)

    # A method to get all services associated with a Master
    def get_services(self):
        return self.services.all()
