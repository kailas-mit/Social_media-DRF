from dataclasses import fields
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import User
from follower.models import Followers

#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "first_name", "last_name", "username"]


# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password')
#         extra_kwargs = {'password': {'write_only': True}}


#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password', 'password2',
         'email', 'first_name', 'last_name')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
    print(validated_data)
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user


class ProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source = 'get_followers_count', read_only=True)
    following_count = serializers.IntegerField(source = 'get_following_count', read_only=True)
    # profile_belongs_to_authenticated_user = serializers.BooleanField(source = 'get_profile_belongs_to_authenticated_user',read_only=True)
    # follow_status = serializers.CharField(source = 'get_follow_status',read_only=True)

    class Meta:
        model= User
        fields = ['id','username','first_name','last_name','email','profile_image','blood_group','bio','location','followers_count','following_count']
        # fields = '__all__'
        read_only_fields = ['id','username']

    # def get_followers_count(self):
    #     return Followers.objects.filter(user = self.user).exclude(is_followed_by = self.user).count()

    # def get_following_count(self):
    #     return Followers.objects.filter(is_followed_by = self.user).count()


































        


    # def update(self, instance, validated_data):
    #     instance.username = validated_data.get('username',instance.username)
    #     print('instance of username',instance.username)
    #     return instance 

    