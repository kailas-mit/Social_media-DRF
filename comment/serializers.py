from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comment,Reply

class CommentSerializer(serializers.ModelSerializer):
    commented_by=serializers.ReadOnlyField(source='user.username')
    class Meta:
        model= Comment
        fields=('id','comment','comment_image','comment_date','commented_by','post')


class ReplySerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Reply
        fields = ['sender', 'receiver', 'message', 'timestamp']
