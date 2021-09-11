from django.urls import path

from .views import LikeInfo

urlpatterns = [
    path('analytics/', LikeInfo.as_view()),
    ]