from django.urls import path
from . import views


urlpatterns = [
    path('barber_profile/', views.barber_profile, name='barber_profile'),
    path('appointment/', views.appointment, name='appointment'),
    
    path('test/', views.test, name='testsar'),
        
]