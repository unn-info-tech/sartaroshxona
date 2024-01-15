from django.contrib import admin
from .models import Country, Region, District, City

# Register your models here.
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(City)

