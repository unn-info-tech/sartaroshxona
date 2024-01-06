from django.urls import path
from . import views

urlpatterns = [
    path('client_profile/', views.client_profile, name='client_profile'),
    # Add more URLs as needed
]
