from django.db import models
from django.contrib.auth.models import User

from post.models import Post

class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment=models.CharField(max_length=3000)
    comment_image=models.ImageField(upload_to='comment_image',null=True, blank=True)
    comment_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.comment


class Reply(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    receiver= models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
    message=models.CharField(max_length=400)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message































    # class Message(models.Model):
    #   sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    #   receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    #   message = models.CharField(max_length=1200)
    #   timestamp = models.DateTimeField(auto_now_add=True)
    #   is_read = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.message
