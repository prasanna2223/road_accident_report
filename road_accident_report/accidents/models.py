from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Accident(models.Model):
    user = models.ForeignKey(
settings.AUTH_USER_MODEL,
    
on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='accidents'
    )

    reporter_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    accident_date = models.DateField(null=True, blank=True)
    accident_time = models.TimeField(null=True, blank=True )

    vehicle_type = models.CharField(max_length=20)
    severity = models.CharField(max_length=10)
    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=10,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user:
            return f"{self.user.username} - {self.location}"
        return self.location
