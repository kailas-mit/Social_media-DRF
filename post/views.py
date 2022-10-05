from django.shortcuts import render
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication



class Postview(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset=Post.objects.all()
    serializer_class= PostSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class Postdetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

