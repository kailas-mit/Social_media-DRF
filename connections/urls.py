from django.urls import include,path
from .views import Connectionview,Request_view,Request_views,Request_accept_view,contact,FriendsConnect,Userlistview

urlpatterns = [
    path('sent/',Connectionview.as_view(), name='connections'),
    path('received/',Request_view.as_view(), name='connected'),
    path('accept/<int:pk>/',Request_views.as_view()),
    path('accepted/',Request_accept_view.as_view()),
    path('contact/',contact.as_view()),
    path('fri/',FriendsConnect.as_view()),
    path('user/',Userlistview.as_view()),
    
]