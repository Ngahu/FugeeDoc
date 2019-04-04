from django.contrib import admin
from .models import HealthOfficer



class HealthOfficerAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'timestamp'
    ]














admin.site.register(HealthOfficer,HealthOfficerAdmin)