from django.contrib import admin
from django.urls import path
from .views import home,LoginView,register

urlpatterns=[
    path('',home,name='home-page'),
    path('login/',LoginView,name='login-page'),
    path('register/',register,name='register-page')
]