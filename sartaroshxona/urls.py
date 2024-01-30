from django.urls import path
from . import views


urlpatterns = [
    path('barber_profile/', views.barber_profile, name='barber_profile'),
    path('workplace/<str:category>/', views.appointments_by_category, name='appointments_by_category'),
    path('accept_and_done_appointment/<int:appointment_id>/', views.accept_and_done_appointment, name='accept_and_done_appointment'),
    path('cancel_appointment/<int:appointment_id>/<str:category>/', views.cancel_appointment, name='cancel_appointment'),

    path('toggle_barber_status/', views.toggle_barber_status, name='toggle_barber_status'),

    path('test/', views.test, name='testsar'),
        
]