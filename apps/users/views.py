from rest_framework import generics

from apps.users.models import User
from apps.users.serializers import UserCreateSerializer, UserDetailSerializer
from apps.users.permissions import IsOwner


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsOwner]


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
