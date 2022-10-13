from comment.serializers import CommentSerializer
from .models import Post
from rest_framework import serializers
from like.serializers import LikeSerializer
from user_auth.models import User

from user_auth.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many= True, read_only=True)
    likes=LikeSerializer(many=True, read_only=True)
    user=UserSerializer(read_only=True)
   
    # likes_count = serializers.IntegerField(source='get_likes_count', read_only = True)
    # comments_count = serializers.IntegerField(source='get_comments_count', read_only = True)
    class Meta:
        model= Post
        fields =('id','user','content', 'post_image', 'category', 'post_date','comments','likes')




        