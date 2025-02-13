from django.db import models
import uuid 

# Create your models here.
class Users(models.Model):
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
     email = models.EmailField(unique=True)
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     created_at = models.DateTimeField(auto_now=True)
     updated_at = models.DateTimeField(auto_now=True)
     
     def __str__(self):
          return self.email