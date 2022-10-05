
from rest_framework import serializers
from .models import Like

# class VotesSerializer(serializers.ModelSerializer):
#     liked_by=serializers.ReadOnlyField(source='liked_by.username')
#     diss_liked_by=serializers.ReadOnlyField(source='diss_liked_by.username')
#     class Meta:
#         model= Votes
#         fields=('id', 'post', 'liked_by', 'diss_liked_by')


class LikeSerializer(serializers.ModelSerializer):
    liked_by=serializers.ReadOnlyField(source='liked_by.username')
    # likes_count = serializers.IntegerField(source='get_likes_count', read_only = True)
    # dislikes_count = serializers.IntegerField(source='get_dislikes_count', read_only = True)
    class Meta:
        model= Like
        fields=('id', 'post', 'liked_by','like', 'like_type')

    
