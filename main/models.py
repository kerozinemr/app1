from django.db import models
from django.contrib.auth.models import User
from storages.backends.s3boto3 import S3Boto3Storage

# Create your models here.
class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null = True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    img = models.ImageField(storage=S3Boto3Storage(),null=True,upload_to='profile_images/')
    
    
    def __str__(self):
        return self.name
    




class Task(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.title
