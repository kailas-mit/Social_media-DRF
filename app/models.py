
from ast import Pass
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    blood_group=models.TextField(blank=True)
    location= models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

    

