from tkinter import CASCADE
from django.db import models
from user_auth.models import User

class Connection(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE, related_name='req_sender')
    receiver=models.ForeignKey(User,on_delete=models.CASCADE, related_name='req_receiver')
    status=models.CharField(max_length=200,default='pending')


    def __str__(self):
        return f"{self.id}--{self.sender}--{self.receiver}"


    


