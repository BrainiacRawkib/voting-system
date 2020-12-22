from django.contrib import admin
from .models import Party


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_link = ['id', 'name']

