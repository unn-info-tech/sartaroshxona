from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, verbose_name="Region/State/Province")

    def __str__(self):
        return self.name


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, verbose_name="District/County")

    def __str__(self):
        return self.name


class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, verbose_name="City/Town/Village")

    def __str__(self):
        return self.name
