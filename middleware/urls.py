from django.urls import path

from .views import UserRequestsView


urlpatterns = [
    path('', UserRequestsView.as_view()),
    ]