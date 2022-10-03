from dataclasses import fields

from comment.serializers import CommentSerializer
from .models import Post
from rest_framework import serializers
from votes.serializers import VotesSerializer

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many= True, read_only=True)
    votes=VotesSerializer(many=True, read_only=True)
    class Meta:
        model= Post
        fields =('id','content', 'post_image', 'category', 'post_date', 'comments', 'votes')