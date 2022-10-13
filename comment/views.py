from email import message
from django.dispatch import receiver
from django.shortcuts import render
# from requests import request
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Comment,Reply
from .serializers import CommentSerializer,ReplySerializer
from rest_framework.authentication import TokenAuthentication


class Commentview(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Comment.objects.all()
    serializer_class= CommentSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class commentdetailview(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Comment.objects.all()
    serializer_class= CommentSerializer


class Replycommentview(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Reply.objects.all()
    serializer_class=ReplySerializer
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)





