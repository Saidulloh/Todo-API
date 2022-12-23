from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.todo.models import Todo
from apps.todo.serializers import TodoSerializer
from apps.todo.permissions import IsOwner


class TodoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class TodoListCreateAPIView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    filter_fields = [
        'title',
        'is_completed',
        'created_at'
    ]
    ordering_fields = [
        'title',
        'is_completed',
        'created_at'
    ]
    search_fields = [
        'title',
        '=created_at'
    ]

    def get_queryset(self):
        title = self.request.query_params.get('title')
        created_at = self.request.query_params.get('created_at')
        if title and created_at:
            queryset = Todo.objects.filter(owner_id=self.request.user.id, title=title, created_at=created_at)
        elif title:
            queryset = Todo.objects.filter(owner_id=self.request.user.id, title=title)
        elif created_at:
            queryset = Todo.objects.filter(owner_id=self.request.user.id, created_at=created_at)
        else:
            queryset = Todo.objects.filter(owner_id=self.request.user.id)
        return queryset

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class DeleteAllTasksAPIView(DestroyAPIView, ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(owner_id=self.request.user.id)

    def destroy(self, request, *args, **kwargs):
        todo = Todo.objects.filter(owner_id=request.user.id)
        for instance in todo:
            self.perform_destroy(instance)
        return Response({'DELETED': 'You are successfully deleted all your tasks!'})
