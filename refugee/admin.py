import site

from django.contrib import admin

# Register your models here.
from .models import Refugee


class RefugeeAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'refugee_id',
        'timestamp'
    ]


admin.site.register(Refugee,RefugeeAdmin)