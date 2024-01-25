from django.urls import path
from . import views

urlpatterns = [
    path('client_profile/', views.client_profile, name='client_profile'),
    path('barbers_list/', views.barbers_list, name='barbers_list'),
    path('favorites/', views.favorites, name='favorites'),
    path('appointment/<int:barber_id>/', views.appointment, name='appointment'),
    path('update_favorites/<int:barber_id>/', views.update_favorites, name='update_favorites'),
    #path('test/', views.test, name='test'),

    # Add more URLs as needed
]
