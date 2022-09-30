from django.urls import URLPattern, path
from .views import follow,Following,Followers

urlpatterns = [
    path('follow/<int:pk>/',follow, name='follow'),
    path('following/<int:pk>/', Following.as_view(), name='following'),
    path('followers/<int:pk>/', Followers.as_view(), name='followers'),
]