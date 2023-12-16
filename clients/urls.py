from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    
    path('test/', views.test, name='testcl'),
        
]