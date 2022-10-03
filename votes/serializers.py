from dataclasses import fields
from rest_framework import serializers
from .models import Votes,Like

class VotesSerializer(serializers.ModelSerializer):
    liked_by=serializers.ReadOnlyField(source='liked_by.username')
    diss_liked_by=serializers.ReadOnlyField(source='diss_liked_by.username')
    class Meta:
        model= Votes
        fields=('id', 'post', 'liked_by', 'diss_liked_by')


class LikeSerializer(serializers.ModelSerializer):
    liked_by=serializers.ReadOnlyField(source='liked_by.username')
    class Meta:
        model= Like
        fields=('id', 'post', 'liked_by','like', 'like_type')

    
