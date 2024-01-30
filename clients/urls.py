from django.urls import path
from . import views

urlpatterns = [
    path('client_profile/', views.client_profile, name='client_profile'),
    path('barbers_list/', views.barbers_list, name='barbers_list'),
    path('favorites/', views.favorites, name='favorites'),
    path('my_appointments/', views.my_appointments, name='my_appointments'),
    path('appointment/<uuid:barber_id>/', views.appointment, name='appointment'),
    path('update_favorites/<uuid:barber_id>/', views.update_favorites, name='update_favorites'),
    #path('test/', views.test, name='test'),

    # Add more URLs as needed
]
