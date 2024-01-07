from django.urls import path
from . import views


urlpatterns = [
    path('barber_profile/', views.barber_profile, name='barber_profile'),
    path('barber_appointments/', views.barber_appointments, name='barber_appointments'),
    path('confirm_appointment/<int:appointment_id>/', views.confirm_appointment, name='confirm_appointment'),


    path('test/', views.test, name='testsar'),
        
]