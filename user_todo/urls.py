from django.urls import path

from .views import (
    apiOverview,
    TodoView,
    TodoDetail,
    TodoCreate,
    TodoUpdate,
    TodoDelete,
)


urlpatterns = [
    path('', apiOverview, name="api-overview"),
    path('todos/',  TodoView.as_view()),
    path('todos/<int:pk>/',  TodoDetail.as_view()),
    path('todos/<int:pk>/like/',  TodoDetail.as_view(), name="like"),
    path('todos/create', TodoCreate.as_view()),
    path('todos/update/<int:pk>/', TodoUpdate.as_view()),
    path('todos/delete/<int:pk>/', TodoDelete.as_view()),
]
