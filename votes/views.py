from django.shortcuts import render
from rest_framework import generics
from .models import Votes
from .serializers import VotesSerializer


# class Votesview(generics.ListCreateAPIView):
#     queryset=Votes.objects.all()
#     serializer_class=VotesSerializer








































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