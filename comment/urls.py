from django.urls import URLPattern, path
from .views import Commentview,commentdetailview

urlpatterns = [
  path('comment/',Commentview.as_view()),
  path('comment/<int:pk>',commentdetailview.as_view()),
]