from django.shortcuts import get_object_or_404, render
from rest_framework import generics,permissions
from .models import Like
from .serializers import LikeSerializer
from .permissions import hasSelfVotedOrReadonly
from django.core.exceptions import ValidationError
from rest_framework import serializers
from post.models import Post
from rest_framework.response import Response
from rest_framework import status
from .permissions import hasSelfVotedOrReadonly
from rest_framework.authentication import TokenAuthentication





class Likesview(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    queryset=Like.objects.all()
    serializer_class=LikeSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,hasSelfVotedOrReadonly]
    def post(self, request, *args, **kwargs):
        if request.data.get('post'):
            post_instance=get_object_or_404(Post,pk=request.data['post'])
            if Like.objects.filter(post=post_instance,liked_by=request.user).exists():
                like_obj = Like.objects.filter(post=post_instance,liked_by=request.user).first()
                if request.data['like_type'] == like_obj.like_type:
                    like_obj.delete()
                    return Response({'success':'Your liked  Have Removed for This Post'},status=status.HTTP_200_OK)
                else:
                    like_obj.like_type = request.data['like_type']
                    like_obj.save()
                    return Response({'success':'Your liked  Have Successfully Changed for This Post'},status=status.HTTP_200_OK)
            else:
                Like.objects.create(post=post_instance,liked_by=request.user,like_type=request.data['like_type'])
                return Response({'success':'You Have Successfully liked This Post'},status=status.HTTP_200_OK)
        return Response({'post':'This Field must be required','like_type':'This Field must be required'},status=status.HTTP_400_BAD_REQUEST)
