from django.urls import path
from . import views

urlpatterns = [
    path('client_profile/', views.client_profile, name='client_profile'),
    path('barbers_list/', views.barbers_list, name='barbers_list'),
    path('appointment/<int:barber_id>/', views.appointment, name='appointment'),

    # Add more URLs as needed
]
