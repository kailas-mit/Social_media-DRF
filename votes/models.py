from django.db import models
from post.models import Post
from django.contrib.auth.models import User
from django_currentuser.middleware import get_current_authenticated_user




class Like(models.Model):
    post = models.ForeignKey(Post, related_name="likes",on_delete = models.CASCADE)
    liked_by = models.ForeignKey(User, related_name = "liked_users", on_delete = models.CASCADE)
    like = models.BooleanField(default = True)
    like_type = models.IntegerField()




    def __str__(self):
        return f"{self.liked_by}--{self.post}"

    













# class Votes(models.Model):
#     post=models.ForeignKey(Post, related_name='votes',on_delete=models.CASCADE)
#     liked_by=models.ForeignKey(User, related_name='liked_by',on_delete=models.CASCADE,default=None,blank=True,null=True)
#     diss_liked_by=models.ForeignKey(User, related_name='diss_liked_by',on_delete=models.CASCADE,default=None,blank=True,null=True )
#     def __str__(self):
#         return self.post.content





