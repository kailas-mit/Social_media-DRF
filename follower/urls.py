from django.urls import URLPattern, path
from .views import follow_api,followers_api

urlpatterns = [
    path('follow/<int:pk>/',follow_api, name='follow'),
    path('follow/',follow_api),
    # path('following/<int:pk>/', Following_api.as_view(), name='following'),
    path('followers/', followers_api, name='followers'),
]