from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView,Userlogin,Profileview,profiledetailview
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
  path("get-details/",UserDetailAPI.as_view()),
  path('register/',RegisterUserAPIView.as_view()),
  path('login/', Userlogin.as_view(), name='login'),
  path('profile/', Profileview.as_view(), name='profile'),
  path('profile/<int:pk>/', profiledetailview.as_view(), name='profile details'),

  # path('settings/', Profileview.as_view(), name='settings'),
  
]