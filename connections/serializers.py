from rest_framework import serializers

from user_auth.models import User
from .models import Connection
from rest_framework.response import Response
from user_auth.serializers import ProfileSerializer,UserSerializer

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Connection
        fields='__all__'
        extra_kwargs={'sender':{'default': serializers.CurrentUserDefault()}}




class ConnectingSerializer(serializers.ModelSerializer):
    status = serializers.CharField(required=True)
    class Meta:
        model=Connection
        fields='__all__'
        extra_kwargs={'recever':{'default': serializers.CurrentUserDefault()}}


class ContactSerializer(serializers.ModelSerializer):
    # connected=Connection('get_connected')
    class Meta:
        model=User
        fields='__all__'



class FriendSerializer(serializers.ModelSerializer):
    # status=ProfileSerializer(source='user.profile')
    # print(status)
    class Meta:
        model=Connection
        fields='__all__'



class ProfilevSerializer(serializers.ModelSerializer):
    # followers_count = serializers.IntegerField(source = 'get_followers_count', read_only=True)
    # following_count = serializers.IntegerField(source = 'get_following_count', read_only=True)
    # profile_belongs_to_authenticated_user = serializers.BooleanField(source = 'get_profile_belongs_to_authenticated_user',read_only=True)
    # follow_status = serializers.CharField(source = 'get_follow_status',read_only=True)

    class Meta:
        model= User
        fields = ['id','username','first_name','last_name','profile_image','blood_group','bio','location']
        # fields = '__all__'
        read_only_fields = ['id','username']


class Alluserlist(serializers.ModelSerializer):
    status=ConnectionSerializer(read_only=True)
    class Meta:
        model=User
        fields = ['id','username','first_name','last_name','profile_image','bio','location','status']

