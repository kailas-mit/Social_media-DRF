from django.db import models
from post.models import Post
from user_auth.models import User


class Like(models.Model):
    post = models.ForeignKey(Post, related_name="likes",on_delete = models.CASCADE)
    liked_by = models.ForeignKey(User, related_name = "liked_users", on_delete = models.CASCADE)
    like = models.BooleanField(default = True)
    like_type = models.IntegerField()
    
    def __str__(self):
        return f"{self.id}--{self.liked_by}--{self.post}"

    






