from django.contrib import admin
from .models import AnnouncedLGAResult, AnnouncedPUResult


@admin.register(AnnouncedLGAResult)
class AnnouncedLGAResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'lga_name', 'party_abbr', 'party_score', 'agent', 'date']
    list_display_links = ['id', 'lga_name']


@admin.register(AnnouncedPUResult)
class AnnouncedPUResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'pu_id', 'party_abbr', 'party_score', 'agent', 'date']
    list_display_links = ['id', 'pu_id']

