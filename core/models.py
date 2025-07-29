from django.db import models
from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"



import uuid
from django.db import models

class Tracking(models.Model):
    tracking_id = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    current_location = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    item = models.CharField(max_length=100, default='Unknown')     # 👈 Add default
    weight = models.FloatField(default=0.0)                         # 👈 Add default
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tracking_id} - {self.status}"
