from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse

from django.contrib.auth.models import User
from .serializers import FollowersSerializer
from rest_framework import generics, mixins, permissions
from post.models import Post
from .models import Followers
from app.models import Profile
from app.serializers import ProfileSerializer

@login_required
def follow(request, pk):
    user = get_object_or_404(User, pk = pk)
    already_followed = Followers.objects.filter(user = user, is_followed_by = request.user).first()
    if not already_followed:
        new_follower = Followers(user = user, is_followed_by = request.user)
        new_follower.save()
        follower_count = Followers.objects.filter(user = user).count()
        return JsonResponse({'status': 'Following', 'count': follower_count})
    else:
        already_followed.delete()
        follower_count = Followers.objects.filter(user = user).count()
        return JsonResponse({'status': 'Not following', 'count': follower_count})


class Following(generics.ListCreateAPIView):
    serializer_class = FollowersSerializer
    permission_classes = [permissions.IsAuthenticated]
    # queryset= Followers.objects.all()

    def get_queryset(self):
        user = User.objects.get(pk = self.kwargs["pk"])
        print (user)
        return Followers.objects.filter(is_followed_by = user)

class Followers(generics.ListCreateAPIView):
    # queryset = Followers.objects.all()
    serializer_class = FollowersSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = get_object_or_404(User, pk = self.kwargs["pk"])
        return Followers.objects.filter(user = user).exclude(is_followed_by = user)


# class followview(generics.ListCreateAPIView):
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]
#     queryset=Followers.objects.all()
#     serializer_class= FollowersSerializer
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class followingdetailview(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Followers.objects.all()
#     serializer_class=FollowersSerializer
