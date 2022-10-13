from django.dispatch import receiver
from .models import Connection
from .serializers import ConnectionSerializer,ConnectingSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from user_auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,authentication_classes




class Connectionview(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ConnectionSerializer
    queryset=Connection.objects.all()
    def get_queryset(self):
        sender=self.request.user
        print(sender)        
        return self.queryset.filter(sender = self.request.user, status = 'pending')


    
    def post(self, request, *args, **kwargs):
        
        query = request.user.req_sender.all()
        serilizers = ConnectionSerializer(instance=query,many=True) 
        # if  is None: return Response({'error':'need some field'})
        if request is not None and request.method == "POST":
            other_user = User.objects.get(pk=request.data['receiver'])
            print (other_user)
            # req_receiver=User.objects.get(pk=pk)
            sender=request.user
            print(sender)
            # already_requested = Connection.objects.filter(sender = request.user, receiver = other_user).first()
            # if other_user is already_requested: return Response({'error':'they already sent you a request'})
            if sender==other_user: return Response({'error':'bad req'})
            if Connection.objects.filter(sender = other_user, receiver = request.user).exists():
                return Response({'error': "you can't send request to requested person"})
            else:
                connect,created=Connection.objects.get_or_create(sender = request.user, receiver = other_user)
                if created:

                    return Response ({'status': 'request sent'})
                else:
                    return Response({'status': 'request already sent'})
            # already_requested = Connection.objects.filter(sender = request.user, receiver = other_user).first()
            # if other_user is already_requested: return Response({'error':'they already sent you a request'})
            # if not already_requested:
            #     new_request = Connection(sender = request.user, receiver = other_user)
            #     new_request.save()
            #     return Response({'status': 'request sent'})
            # else:
            #     already_requested.delete()
            #     return Response({'status': 'already request sent'})
            

        return Response(serilizers.data,status=status.HTTP_200_OK)








class Request_view(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ConnectingSerializer
    queryset=Connection.objects.all()
    def get_queryset(self):
        receiver=self.request.user
        print(receiver)        
        return self.queryset.filter(receiver = self.request.user, status = 'pending') 

class Request_views(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ConnectingSerializer
    queryset=Connection.objects.all()
    def get_queryset(self):
        receiver=self.request.user
        print(receiver)        
        return self.queryset.filter(receiver = self.request.user) 





class Request_accept_view(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ConnectingSerializer
    queryset=Connection.objects.all()
    def get_queryset(self):
        receiver=self.request.user
        print(receiver)        
        return self.queryset.filter(receiver = self.request.user, status = 'accept') 











    # def get_queryset(self):
    #     receiver=self.request.user
    #     print(receiver)        
    #     return self.queryset.filter(receiver = self.request.user, status = 'pending') 

    # def post(self, request, *args, **kwargs):
    #     # if self.queryset.filter(receiver = self.request.user, status = 'pending'):
    #     # query = request.user.req_receiver.all()
    #     # print(query)
    #     # serilizers = ConnectingSerializer(instance=query,many=True)
    #     if request is not None and request.method == "POST":
    #         req = Connection.objects.filter(receiver = self.request.user, status='pending')
    #         print(req)
    #         # req.accept()
    #         return Response({'message':'good'})
    #     else:
    #         return Response({'message': 'invalid info'})
                
            # print(req)
            # receiver = get_object_or_404(User, pk = pk)
        # if Connection.objects.get(receiver = request.user, sender = sender):
            # return Response({'done'})




# @api_view(['POST','GET'])
# # @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def Get_connected(request, pk=None):
#     connect=Connection.objects.get(pk=pk , status='pending')
#     print(connect)
#     if connect.receiver==request.user and request.method=='POST':
#         connect.receiver.status.add(connect.sender)
#         connect.sender.status.add(connect.receiver)
#         connect.delete()
#         return Response({'message':'now u are connected'})
#     else:
#         return Response({'message':'request not accepted'})






# @api_view(['POST','GET'])
# # @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def connection_api(request, pk= None):
#     query = request.user.req_sender.all()
#     serilizers = ConnectionSerializer(instance=query,many=True)

#     if pk is not None and request.method == "POST":
#         receiver = get_object_or_404(User, pk = pk)
#         sender=request.user
#         print(sender)
#         print(receiver)
#         if sender == receiver: return Response({'error':"Invalid Requests "})
#         already_requested = Connection.objects.filter(sender = request.user, receiver = receiver).first()
#         if not already_requested:
#             new_request = Connection(sender = request.user, receiver = receiver)
#             new_request.save()
#             return Response({'status': 'request sent'})
#         else:
#             already_requested.delete()
#             return Response({'status': 'request not sent'})
#     return Response(serilizers.data,status=status.HTTP_200_OK)







# @api_view(['POST','GET'])
# # @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def Connectionview(request , pk):
#     req_sender=request.user
#     req_receiver=User.objects.get(pk=pk)
#     connect, created =Connection.objects.get_or_create(req_sender=req_sender, req_receiver=req_receiver)
#     if created:
#         return Response({'message':'connect request sent'})
#     else:
#         return Response({'message':'connection request already sent'})













# login:-09:45
# Date:-12/10/2022


# - created send connection request
# - implement in sent request
# - implement in received request
# - working on status of connection
# - cross section sender to receiver and receiver to sender also in progress


# logout:-18:50
