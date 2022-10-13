from pyexpat import model
from rest_framework import serializers
from .models import Followers
from user_auth.serializers import UserSerializer,ProfileSerializer


class FollowerSerializer(serializers.ModelSerializer):
    is_followed_by=ProfileSerializer(read_only=True)
    # user = serializers.DictField(child = serializers.CharField(), source = 'get_user_info', read_only = True)
    # is_followed_by = serializers.DictField(child = serializers.CharField(), source = 'get_is_followed_by_info', read_only = True)
    # followers_count = serializers.IntegerField(source = 'get_followers_count', read_only = True)
    # following_count = serializers.IntegerField(source = 'get_following_count', read_only = True)
    

    class Meta:
        model = Followers
        fields = ('user', 'is_followed_by')
        # read_only_fields = ('user', 'is_followed_by')


class FollowingSerializer(serializers.ModelSerializer):
    user=ProfileSerializer(read_only=True)
    # user = serializers.DictField(child = serializers.CharField(), source = 'get_user_info', read_only = True)
    # is_followed_by = serializers.DictField(child = serializers.CharField(), source = 'get_is_followed_by_info', read_only = True)
    # followers_count = serializers.IntegerField(source = 'get_followers_count', read_only = True)
    # following_count = serializers.IntegerField(source = 'get_following_count', read_only = True)
    

    class Meta:
        model = Followers
        fields = ('user', 'is_followed_by')
        # read_only_fields = ('user', 'is_followed_by')























# def get_follower(self, obj):
#     context = self.context
#     request = context.get("request")
#     return request.user.following_user.all().values()
