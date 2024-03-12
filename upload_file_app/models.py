# myapp/models.py
from django.contrib.auth.models import User
from django.db import models

class UserAccount(models.Model):
    username = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class UploadedData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    # Add other fields as needed

    def __str__(self):
        return self.file.name
    
    
