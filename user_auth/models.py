from django.db import models
from django.contrib.auth.models import AbstractUser
from django_currentuser.middleware import get_current_authenticated_user
# from follower.models import Followers


from django.db import models
# Create your models here.



class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_image',blank=True,null=True)
    blood_group=models.TextField(blank=True)
    bio=models.TextField(blank=True)
    location= models.CharField(max_length=20)
    # connections=models.ManyToManyField("User",blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


    def get_followers_count(self):
        return User.objects.filter(email = self.email).first().user_following.exclude(is_followed_by__email = self.email).all().count()

    def get_following_count(self):
        return User.objects.filter(email = self.email).first().user_followers.exclude(user__email = self.email).all().count()

    # def __str__(self):
    #     return f"{self.id}--{self.username}"

        
    


# class Profile(models.Model):
#     user= models.OneToOneField(User,on_delete=models.CASCADE)
#     bio=models.TextField(blank=True)
#     profile_image=models.ImageField(upload_to='profile_images',null=True, blank=True)
#     blood_group=models.TextField(blank=True)
#     location= models.CharField(max_length=20)
    # following = models.ManyToManyField(User, related_name='followers', blank=True)


    # def get_user_id(self):
    #     return self.user.pk

    # def get_username(self):
    #     return self.user.username

    # def get_followers_count(self):
    #     return Followers.objects.filter(user = self.user).exclude(is_followed_by = self.user).count()

    # def get_following_count(self):
    #     return Followers.objects.filter(is_followed_by = self.user).count()

    # def get_follow_status(self):
    #     follow_status = Followers.objects.filter(user = self.user, is_followed_by = get_current_authenticated_user())
    #     return "Following" if follow_status else "Follow"

    # def get_profile_belongs_to_authenticated_user(self):
    #     return self.user == get_current_authenticated_user()
        
    # def __str__(self):
    #     return str(self.user)

    # def __str__(self):
    #     return self.user.username