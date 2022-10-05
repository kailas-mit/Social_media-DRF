from .views import Likesview
from django.urls import path


urlpatterns = [
  path('like/',Likesview.as_view())
]