from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),
    # path('logout/', logout, {'next_page': 'index'}, name='logout'),
    # path('register/', views.register_view, name='register'),
]

##############

# from django.urls import include,path
# from .views import Chatview,Chatviews

# urlpatterns = [
#     path('message/',Chatview.as_view()),
#     path('rmessage/',Chatviews.as_view())
        
# ]



#########

# from django.urls import path
# from . import views
# urlpatterns = [
#     # URL form : "/api/messages/1/2"
#     path('messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),  # For GET request.
#     # URL form : "/api/messages/"
#     path('messages/', views.message_list, name='message-list'),   # For POST
#     # URL form "/api/users/1"
#     path('users/<int:pk>', views.user_list, name='user-detail'),      # GET request for user with id
#     path('users/', views.user_list, name='user-list'),    # POST for new user and GET for all users list
# ]