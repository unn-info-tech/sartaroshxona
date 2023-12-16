from django.urls import path
from . import views

app_name = 'sartaroshxona'

urlpatterns = [
    path('appointment/', views.appointment, name='appointment'),
    path('sign/', views.sign, name='sign'),
    path('test/', views.test, name='testsar'),
        
]