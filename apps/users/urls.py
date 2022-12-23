from django.urls import path

from apps.users.views import UserRetrieveUpdateDestroyAPIView, UserListAPIView, UserCreateAPIView


urlpatterns = [
    path('<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),
    path('', UserListAPIView.as_view()),
    path('<int:pk>/', UserCreateAPIView.as_view()),
]
