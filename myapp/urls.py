from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'myapp'

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('account',account,name='account'),
    path('UpdateGroupName/',UpdateGroupName,name='UpdateGroupName'),
    path('UpdateScore/',UpdateScore,name='UpdateScore'),
    path('updatePassword/<int:id>',updatePassword,name='updatePassword'),
    path('createusers/',createusers,name='createusers'),
    path('updateUsers/',updateUsers,name='updateUsers'),
    path('resetGame/',resetGame,name='resetGame'),
    path('activateTeams/',activateTeams,name='activateTeams'),
    path('clearTeams/',clearTeams,name='clearTeams'),
]