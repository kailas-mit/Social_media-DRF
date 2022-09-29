from django.shortcuts import render
from requests import request
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer
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




