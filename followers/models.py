from django.db import models
from django.contrib.auth.models import User
from requests import delete

class Followers(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    is_followed_by=models.ForeignKey(User, on_delete=models.CASCADE, related_name='is_followed_by')
