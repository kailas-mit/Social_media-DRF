from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    liked_by=serializers.ReadOnlyField(source='liked_by.username')
    
    class Meta:
        model= Like
        fields=('id', 'post', 'liked_by','like', 'like_type')