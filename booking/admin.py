from django.contrib import admin
from .models import VaccinationCenter, Slot

# Register your models here.

class VaccinationCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'working_hours_start', 'working_hours_end', 'slots', 'dosage')
    list_filter = ('dosage',)

admin.site.register(VaccinationCenter, VaccinationCenterAdmin)
admin.site.register(Slot)
