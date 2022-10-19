from django.contrib.auth import authenticate, login
from user_auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chat.models import Chat
from chat.serializers import ChatSerializer, UserSerializer
from rest_framework.response import Response 


def index(request):
    if request.user.is_authenticated:
        return redirect('chats')
    if request.method == 'GET':
        return Response({'message':"all good"})
    if request.method == "POST":
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return Response('{"error": "User does not exist"}')
        return redirect('chats')



@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Chat.objects.filter(m_sender_id=sender, m_receiver_id=receiver, is_read=False)
        serializer = ChatSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ChatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)





def chat_view(request):
    if not request.user.is_authenticated:
        return Response({'message': 'wait for chat'})
    if request.method == "GET":
        return Response({'users': User.objects.exclude(username=request.user.username)})


def message_view(request, sender, receiver):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, "chat/messages.html",
                      {'users': User.objects.exclude(username=request.user.username),
                       'receiver': User.objects.get(id=receiver),
                       'messages': Chat.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Chat.objects.filter(sender_id=receiver, receiver_id=sender)})










############


# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from .models import Chat
# from .serializers import ChatSerializer

# class Chatview(generics.ListCreateAPIView):
#     permission_classes=[IsAuthenticated]
#     serializer_class=ChatSerializer
#     queryset=Chat.objects.all()
#     def get_queryset(self):
#         # m_sender=self.request.user
#         # print(m_sender)        
#         # if Chat.objects.filter(self.request.m_sender=m_sender,receiver)
#         return self.queryset.filter(m_sender = self.request.user) 

#     # def post(self ,request.*args, **kwrgs):
#     #     pass



# class Chatviews(generics.ListCreateAPIView):
#     permission_classes=[IsAuthenticated]
#     serializer_class=ChatSerializer
#     queryset=Chat.objects.all()
#     def get_queryset(self):
#         return self.queryset.filter(m_receiver=self.request.user)



###############



# from user_auth.models import User                               # Django Build in User Model
# from django.http.response import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from chat.models import Chat                                                   # Our Message model
# from chat.serializers import ChatSerializer, UserSerializer # Our Serializer Classes
# # Users View
# @csrf_exempt                                                              # Decorator to make the view csrf excempt.
# def user_list(request, pk=None):
#     """
#     List all required messages, or create a new message.
#     """
#     if request.method == 'GET':
#         if pk:                                                                      # If PrimaryKey (id) of the user is specified in the url
#             users = User.objects.filter(id=pk)              # Select only that particular user
#         else:
#             users = User.objects.all()                             # Else get all user list
#         serializer = UserSerializer(users, many=True, context={'request': request}) 
#         return JsonResponse(serializer.data, safe=False)               # Return serialized data
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)           # On POST, parse the request object to obtain the data in json
#         serializer = UserSerializer(data=data)        # Seraialize the data
#         if serializer.is_valid():
#             serializer.save()                                            # Save it if valid
#             return JsonResponse(serializer.data, status=201)     # Return back the data on success
#         return JsonResponse(serializer.errors, status=400)     # Return back the errors  if not valid




# @csrf_exempt
# def message_list(request, sender=None, receiver=None):
#     """
#     List all required messages, or create a new message.
#     """
#     if request.method == 'GET':
#         messages = Chat.objects.filter(m_sender_id=sender, m_receiver_id=receiver)
#         serializer = ChatSerializer(messages, many=True, context={'request': request})
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ChatSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
