from django.db import models
from user_auth.models import User



class Followers(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_following')
    is_followed_by=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_followers')



    # def get_user_info(self):
    #     user_dict = vars(self.user)
    #     return {"id": user_dict["id"], "username": user_dict["username"]}

    # def get_is_followed_by_info(self):
    #     user_dict = vars(self.is_followed_by)
    #     return {"id": user_dict["id"], "username": user_dict["username"]}
        
    # def get_following(self, user):
    #     return Followers.objects.filter(is_followed_by=user)

    # def get_followers(self, user):
    #     return Followers.objects.filter(user=user).exclude(is_followed_by=user)

    # def get_following_count(self, user):
    #     return Followers.objects.filter(is_followed_by=user).count()

    # def get_followers_count(self, user):
    #     return Followers.objects.filter(user=user).count()
        
    def __str__(self):
        return f"{self.id}--{self.user}--{self.is_followed_by}"

 

