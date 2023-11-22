from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'login'

urlpatterns = [
    path('',loginMe,name='login'),
    path('signin', signin, name='signin'),
    path('logout/', logoutPage, name='logout'),
]