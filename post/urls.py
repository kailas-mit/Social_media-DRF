from django.urls import path
from . import views


urlpatterns = [
  path('post/',views.Postview.as_view()),
  path('post/<int:pk>/',views.Postdetailview.as_view()),
]