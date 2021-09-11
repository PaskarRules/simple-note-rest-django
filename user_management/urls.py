from django.urls import path

from .views import UserRegistrationView, UserLoginView, UserActivityView

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('activity/<int:pk>/', UserActivityView.as_view())
    ]