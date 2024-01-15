from .models import Country, Region, District, City
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import City, District, Region











# AJAX
def load_regions(request):
    country_id = request.GET.get('country_id')
    regions = Region.objects.filter(country_id=country_id).all()
    return render(request, 'locations/region_dropdown_list_options.html', {'regions': regions})

def load_districts(request):
    region_id = request.GET.get('region_id')
    districts = District.objects.filter(region_id=region_id).all()
    return render(request, 'locations/district_dropdown_list_options.html', {'districts': districts})

def load_cities(request):
    district_id = request.GET.get('district_id')
    cities = City.objects.filter(district_id=district_id).all()
    return render(request, 'locations/city_dropdown_list_options.html', {'cities': cities})