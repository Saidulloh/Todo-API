from rest_framework.viewsets import ModelViewSet

from apps.todo.models import Todo
from apps.todo.serializers import TodoSerializer


class TodoApiViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
