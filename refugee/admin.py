import site

from django.contrib import admin

# Register your models here.
from .models import (
    Refugee,
    PatientSymptom,
    Location,
    Entry
)


class RefugeeAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'refugee_id',
        'timestamp'
    ]


admin.site.register(Refugee,RefugeeAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = [
        'latitude',
        'longitude',
        'village'
    ]


admin.site.register(Location,LocationAdmin)





admin.site.register(PatientSymptom)




class EntryAdmin(admin.ModelAdmin):
    list_display = [
        'entry_id',
        'creator',
        'timestamp'
    ]


admin.site.register(Entry,EntryAdmin)