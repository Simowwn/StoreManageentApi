from django.db import models
import uuid
# from user.models import Users  # Keep this if you still need Users

# Create your models here.

class Stall(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.CharField(max_length=255)
    type = models.CharField(max_length=255)  # This field should exist
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand
    
