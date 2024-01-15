from django.urls import path
from . import views

urlpatterns = [
    #AJAX 
    #path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
    path('ajax/load-regions/', views.load_regions, name='ajax_load_regions'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]
