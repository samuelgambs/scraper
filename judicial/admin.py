from django.contrib import admin
from .models import Process, PartiesInvolved, PartiesInvolvedProcess

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('process_number', 'process_class', 'subject', 'judge')
    search_fields = ('process_number', 'process_class', 'subject', 'judge')

@admin.register(PartiesInvolved)
class PartiesInvolvedAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category')

@admin.register(PartiesInvolvedProcess)
class PartiesInvolvedProcessAdmin(admin.ModelAdmin):
    list_display = ('process', 'parties_involved')
    search_fields = ('process', 'parties_involved')

