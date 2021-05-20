from django.contrib import admin
from django.urls import path
from .views import home,LoginView,register,EventRegister,LogoutView,DefineView,add_to_cart

urlpatterns=[
    path('',home,name='home-page'),
    path('login/',LoginView,name='login-page'),
    path('register/',register,name='register-page'),
    path('event_register/',EventRegister,name='event-register-page'),
    path('logout/',LogoutView,name='logout-page'),
    path('event-model/<int:id>/',DefineView,name='model-define'),
    path('add-to-cart/<int:id>/',add_to_cart,name='add-to-cart')
]