from .views import Votesview
from django.urls import path


urlpatterns = [
  path('vote/',Votesview.as_view())
]