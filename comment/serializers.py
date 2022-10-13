from rest_framework import serializers
from user_auth.models import User

from .models import Comment,Reply





class ReplySerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Reply
        # fields = ['comments','sender', 'receiver', 'message', 'timestamp']
        fields = "__all__"




class CommentSerializer(serializers.ModelSerializer):
    commented_by=serializers.ReadOnlyField(source='user.username')
    reply=ReplySerializer(many=True, read_only=True)
    
    class Meta:
        model= Comment
        fields=('id','comment','comment_date','commented_by','post', 'reply')
