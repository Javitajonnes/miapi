from django.urls import pathfro
from .views import(TodoListApiView,
                   )

urlpatterns = [
    path('api', TodoListApiView.as_view())
]