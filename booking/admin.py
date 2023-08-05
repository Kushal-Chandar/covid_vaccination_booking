from django.contrib import admin

# Register your models here.
from .models import VaccinationCenter, Slot

admin.site.register(VaccinationCenter)
admin.site.register(Slot)
