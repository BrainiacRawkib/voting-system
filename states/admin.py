from django.contrib import admin
from .models import State, LGA, Ward, PollingUnit


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


@admin.register(LGA)
class LGAAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'state']
    list_display_links = ['id', 'name']


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'lga', 'state']
    list_display_links = ['id', 'name']


@admin.register(PollingUnit)
class PollingUnitAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'lga', 'state', 'agent']
    list_display_links = ['id', 'name']
