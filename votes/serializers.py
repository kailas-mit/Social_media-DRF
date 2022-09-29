from dataclasses import fields
from rest_framework import serializers
from .models import Votes

class VotesSerializer(serializers.ModelSerializer):
    up_vote_by=serializers.ReadOnlyField(source='up_vote_by.username')
    down_vote_by=serializers.ReadOnlyField(source='down_vote_by.username')
    class Meta:
        model= Votes
        fields=('id', 'post', 'up_vote_by', 'down_vote_by')