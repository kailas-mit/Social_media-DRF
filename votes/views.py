from django.shortcuts import get_object_or_404, render
from requests import post
from rest_framework import generics,permissions
from .models import Like
from .serializers import LikeSerializer
from .permissions import hasSelfVotedOrReadonly
from django.core.exceptions import ValidationError
from rest_framework import serializers
from post.models import Post
from rest_framework.response import Response
from rest_framework import status





class Likesview(generics.ListCreateAPIView):
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





        #     like_obj = Like.objects.filter(post=post_instance,liked_by=self.request.user).first()
        #     like_obj.delete()
        #     if already_liked:
        #         raise serializers.ValidationError({"message":"you have already liked this post"})
        #     else:
        #         serializer.save(liked_by=self.request.user,post=post_instance)

        # else:
        #     already_liked=Votes.objects.filter(post=post_instance,liked_by=self.request.user).exists()
        #     if already_liked:
        #         raise serializers.ValidationError({"message":"you have already liked this post"})

        #     already_diss_liked=Votes.objects.filter(post=post_instance,diss_liked_by=self.request.user).exists()
        #     if already_diss_liked:
        #         raise serializers.ValidationError({"message":"you have already liked this post"})
                
        #     else:
        #         serializer.save(diss_liked_by=self.request.user,post=post_instance)


        
        # # else:
        # #     already_liked=Votes.objects.filter(post=post_instance,liked_by=self.request.user).exists()
        # #     already_diss_liked=Votes.objects.filter(post=post_instance,diss_liked_by=self.request.user).exists()
        # #     if already_diss_liked:
        # #         if already_liked:
        # #             raise serializers.ValidationError({"message":"you have already liked this post"})
        # #         raise serializers.ValidationError({"message":"you have already diss liked this post"})
        # #     else:
        # #         serializer.save(diss_liked_by=self.request.user,post=post_instance)
            

        # return super().perform_create(serializer)



        # class Votesview(generics.ListCreateAPIView):
#     queryset=Votes.objects.all()
#     serializer_class=VotesSerializer
#     permission_classes=[permissions.IsAuthenticatedOrReadOnly,hasSelfVotedOrReadonly]
#     def perform_create(self, serializer):
#         post_instance=get_object_or_404(Post,pk=self.request.data['post'])
#         if self.request.data['post']:
#             already_liked=Votes.objects.filter(post=post_instance,liked_by=self.request.user).exists()
#             if already_liked:
#                 raise serializers.ValidationError({"message":"you have already liked this post"})
#             else:
#                 serializer.save(liked_by=self.request.user,post=post_instance)

#         else:
#             already_liked=Votes.objects.filter(post=post_instance,liked_by=self.request.user).exists()
#             if already_liked:
#                 raise serializers.ValidationError({"message":"you have already liked this post"})

#             already_diss_liked=Votes.objects.filter(post=post_instance,diss_liked_by=self.request.user).exists()
#             if already_diss_liked:
#                 raise serializers.ValidationError({"message":"you have already liked this post"})
                
#             else:
#                 serializer.save(diss_liked_by=self.request.user,post=post_instance)


        
        # else:
        #     already_liked=Votes.objects.filter(post=post_instance,liked_by=self.request.user).exists()
        #     already_diss_liked=Votes.objects.filter(post=post_instance,diss_liked_by=self.request.user).exists()
        #     if already_diss_liked:
        #         if already_liked:
        #             raise serializers.ValidationError({"message":"you have already liked this post"})
        #         raise serializers.ValidationError({"message":"you have already diss liked this post"})
        #     else:
        #         serializer.save(diss_liked_by=self.request.user,post=post_instance)
            

        # return super().perform_create(serializer)




































'''
login:-10:00

API
-tried to make inter-relation between like,post and user 
-worked on reverse query
-succefully fetch like for particular post
-started working on comment section

logout:-19:05
'''