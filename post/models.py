from email.policy import default
from django.db import models
from user_auth.models import User

from django_currentuser.middleware import get_current_authenticated_user


class Post(models.Model):
    user=models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    content=models.CharField(max_length=4000)
    post_image=models.ImageField(upload_to="post_image", null=True, blank=True)
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=3000,default=None,null= True, blank=True)
    '''category will replace by post created by'''

    # def get_readable_date(self):
    #     return self.pub_date.strftime("%B %d, %Y")

    # def get_post_belongs_to_authenticated_user(self):
    #     return self.posted_by.pk == get_current_authenticated_user().pk

    # def get_user(self):
    #     user_dict = vars(self.posted_by)
    #     return {"id": user_dict["id"], "username": user_dict["username"]}

    # def get_likes_count(self):
    #     return Like.objects.filter(liked=True, rated_post=self).count()

    # def get_dislikes_count(self):
    #     return Like.objects.filter(liked=False, rated_post=self).count()

    # def get_comments(self):
    #     return Post.objects.filter(in_reply_to_post=self.pk)

    # def get_comments_count(self):
    #     return Post.objects.filter(in_reply_to_post=self.pk).count()

    # def __str__(self):
    #     return str(self)

    

    def __str__(self):
        return f"{self.id}--{self.user}--{self.content}"


        
