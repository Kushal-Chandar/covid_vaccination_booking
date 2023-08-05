from django.contrib import admin

# Register your models here.
from .models import VaccinationCenter, UserProfile

admin.site.register(VaccinationCenter)
admin.site.register(UserProfile)
