from .models import Followers
from .serializers import FollowerSerializer,FollowingSerializer
from django.shortcuts import  get_object_or_404
from user_auth.models import User
from rest_framework import generics,permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@api_view(['POST','GET'])
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def follow_api(request, pk= None):
    query = request.user.user_following.all()
    serilizers = FollowerSerializer(instance=query,many=True)

    if pk is not None and request.method == "POST":
        other_user = get_object_or_404(User, pk = pk)
        if request.user == other_user: return Response({'error':"Invalid Requests You can't follow yourself"})
        already_followed = Followers.objects.filter(user = request.user, is_followed_by = other_user).first()
        if not already_followed:
            new_follower = Followers(user = request.user, is_followed_by = other_user)
            new_follower.save()
            following_count = Followers.objects.filter(user = request.user).count()
            return Response({'status': 'Following', 'count': following_count})
        else:
            already_followed.delete()
            following_count = Followers.objects.filter(user = request.user).count()
            return Response({'status': 'Not following', 'count': following_count})
    return Response(serilizers.data,status=status.HTTP_200_OK)



@api_view(['POST','GET'])
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def followers_api(request):
    query = request.user.user_followers.all()
    serilizers = FollowingSerializer(instance=query,many=True)
    return Response(serilizers.data,status=status.HTTP_200_OK)
    




# class Following_api(generics.ListCreateAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = FollowerSerializer

#     def get_queryset(self):
#         user = User.objects.get(pk = self.kwargs["pk"])
#         print (user)
#         return Followers.objects.filter(is_followed_by = user)

    
# class Followers_Api(generics.ListCreateAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Followers.objects.all()
#     serializer_class = FollowerSerializer
    

#     def get_queryset(self):
#         user = get_object_or_404(User, pk = self.kwargs["pk"])
#         return Followers.objects.filter(user = user).exclude(is_followed_by = user)


# class AddFollower(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated ]
#     def post(self, requset, format=None):
#         user = User.objects.get(user_id=self.request.data.get('user_id'))
#         print (user)
#         follow = User.objects.get(user_id=self.request.data.get('follow'))
#         user.following.add(follow)
#         user.save()
#         follow.followers.add(user)
#         follow.save()
#         print(str(user) + ", " + str(follow))
#         return JsonResponse({'status':status.HTTP_200_OK, 'data':"", 'message':"follow"+str(follow.user_id)})


# class Follow(generics.ListCreateAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = FollowerSerializer
#     @csrf_exempt

#     def follow(request, pk):
#         other_user = get_object_or_404(User, pk = pk)
#         already_followed = Followers.objects.filter(user = request.user, is_followed_by = other_user).first()
#         if not already_followed:
#             new_follower = Followers(user = request.user, is_followed_by = other_user)
#             new_follower.save()
#             following_count = Followers.objects.filter(user = request.user).count()
#             return Response({'status': 'Following', 'count': following_count})
#         else:
#             already_followed.delete()
#             following_count = Followers.objects.filter(user = request.user).count()
#             return Response({'status': 'Not following', 'count': following_count})