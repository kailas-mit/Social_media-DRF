from django.shortcuts import get_object_or_404, render
from requests import post
from rest_framework import generics,permissions
from .models import Votes
from .serializers import VotesSerializer
from .permissions import hasSelfVotedOrReadonly
from django.core.exceptions import ValidationError
from rest_framework import serializers


class Votesview(generics.ListCreateAPIView):
    queryset=Votes.objects.all()
    serializer_class=VotesSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,hasSelfVotedOrReadonly]
    def perform_create(self, serializer):
        post_instance=get_object_or_404(post,pk=self.request.data['post'])
        if self.request.data['up_vote']:
            already_up_voted=Votes.objects.filter(post=post_instance,up_vote_by=self.request.user).exists()
            if already_up_voted:
                raise serializers.ValidationError({"message":"you have already liked this post"})
            else:
                serializer.save(up_vote_by=self.request.user,post=post_instance)
        else:
            already_down_voted=Votes.objects.filter(post=post_instance,down_vote_by=self.request.user).exists()
            if already_down_voted:
                raise serializers.ValidationError({"message":"you have already liked this post"})
            else:
                serializer.save(down_vote_by=self.request.user,post=post_instance)
            

        return super().perform_create(serializer)








































'''
login:-09:30

API
-Implemented Profileview Api
    Models, Serializers, views, Urls
    added some fields
-Implemented postcreate Api
-Implemented commentview Api

logout:-18:40
'''