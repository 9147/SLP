from django.contrib import admin
from .models import *

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id','name','leader','score')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id','status')
