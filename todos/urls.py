from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ips/', include('middleware.urls')),
    path('api-user/', include('user_management.urls')),
    path('api-todo/', include('user_todo.urls')),
    path('api/', include('analytics.urls')),
]
