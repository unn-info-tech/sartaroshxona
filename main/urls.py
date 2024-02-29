from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.log_out, name='logout'),
    path('delete_account/', views.delete_account, name='delete_account'),
    

    path('ads_list/', views.ads_list, name='ads_list'),
    path('others/', views.others, name='others'),
    path('tospp/', views.tospp, name='tospp'),
    path('contact_dev/', views.contact_dev, name='contact_dev'),

    path('feedback/', views.feedback, name='feedback'),
    

    path('middleware/', views.middleware, name='middleware'),







    

    #===========================================
]
