import profile
from urllib import request
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer,ProfileSerializer
# from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import obtain_auth_token,ObtainAuthToken
from rest_framework import generics
from rest_framework.authtoken.models import Token
from .models import User
from rest_framework import permissions
from .models import get_current_authenticated_user


# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer



class Userlogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        context = {
            "user_id":user.id,
            "user_name":user.username,
            "token":token.key,
            }
        return Response(context)


class Profileview(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class= ProfileSerializer
    queryset=User.objects.all()
    def get(self, request, *args, **kwargs):
      obj = request.user
      return Response (self.serializer_class(instance=obj).data)




class UserIsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
    


class profiledetailview(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,UserIsOwnerOrReadOnly]
    queryset=User.objects.all()
    serializer_class= ProfileSerializer


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    # def put(self, request, *args, **kwargs):
    #   obj = request.user
    #   return Response (self.serializer_class(instance=obj).data)



    
































# class DetailView(APIView):
#     def get_object(self, pk):
#         return TestModel.objects.get(pk=pk)

#     def patch(self, request, pk):
#         testmodel_object = self.get_object(pk)
#         serializer = TestModelSerializer(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(code=201, data=serializer.data)
#         return JsonResponse(code=400, data="wrong parameters")


# class UpdateAPIView(mixins.UpdateModelMixin,
#                     GenericAPIView):
#     """
#     Concrete view for updating a model instance.
#     """
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)


