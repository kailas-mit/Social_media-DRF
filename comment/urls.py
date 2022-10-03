from django.urls import URLPattern, path
from .views import Commentview,commentdetailview,Replycommentview

urlpatterns = [
  path('comment/',Commentview.as_view()),
  path('comment/<int:pk>',commentdetailview.as_view()),
  path('comment/reply/',Replycommentview.as_view()),
]