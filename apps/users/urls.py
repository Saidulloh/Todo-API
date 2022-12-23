from django.urls import path

from apps.users.views import UserRetrieveUpdateDestroyAPIView, UserListCreateAPIView


urlpatterns = [
    path('<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),
    path('', UserListCreateAPIView.as_view()),
]
