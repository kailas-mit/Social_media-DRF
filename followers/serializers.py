from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Followers

class FollowersSerializer(serializers.ModelSerializer):
    user = serializers.DictField(child = serializers.CharField(), source = 'get_user_info', read_only = True)
    is_followed_by = serializers.DictField(child = serializers.CharField(), source = 'get_is_followed_by_info', read_only = True)
    # followers_count = serializers.IntegerField(source = 'get_followers_count')
    # following_count = serializers.IntegerField(source = 'get_following_count')
    # follow_status = serializers.CharField(source = 'get_follow_status')

    class Meta:
        model = Followers
        fields = ('user', 'is_followed_by')
        read_only_fields = ('user', 'is_followed_by')