from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('data/',data,name='data'),
]