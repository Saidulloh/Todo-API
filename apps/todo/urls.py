from django.urls import path

from apps.todo.views import TodoRetrieveUpdateDestroyAPIView, TodoListCreateAPIView, DeleteAllTasksAPIView


urlpatterns = [
    path('<int:pk>/', TodoRetrieveUpdateDestroyAPIView.as_view()),
    path('', TodoListCreateAPIView.as_view()),
    path('delete/', DeleteAllTasksAPIView.as_view())
]
