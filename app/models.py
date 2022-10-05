
from ast import Pass
from distutils.command.upload import upload
import profile
import django
from django.db import models
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import get_current_authenticated_user
from followers.models import Followers
class Profile(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    profile_image=models.ImageField(upload_to='profile_images',null=True, blank=True)
    blood_group=models.TextField(blank=True)
    location= models.CharField(max_length=20)
    # following = models.ManyToManyField(User, related_name='followers', blank=True)


    def get_user_id(self):
        return self.user.pk

    def get_username(self):
        return self.user.username

    def get_followers_count(self):
        return Followers.objects.filter(user = self.user).exclude(is_followed_by = self.user).count()

    def get_following_count(self):
        return Followers.objects.filter(is_followed_by = self.user).count()

    def get_follow_status(self):
        follow_status = Followers.objects.filter(user = self.user, is_followed_by = get_current_authenticated_user())
        return "Following" if follow_status else "Follow"

    def get_profile_belongs_to_authenticated_user(self):
        return self.user == get_current_authenticated_user()
        
    def __str__(self):
        return str(self.user)

    # def __str__(self):
    #     return self.user.username



    

