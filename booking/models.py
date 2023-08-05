from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class VaccinationCenter(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically incrementing primary key
    name = models.CharField(max_length=100)
    working_hours_start = models.TimeField(default="00:00")
    working_hours_end = models.TimeField(default="00:00")
    slots = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.name}, {self.working_hours_start} - {self.working_hours_end}, {self.slots}"

class Slot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    center = models.ForeignKey(VaccinationCenter, on_delete=models.CASCADE)

    def __str__(self):
        return f"Slot for {self.user.username} at {self.center.name}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
