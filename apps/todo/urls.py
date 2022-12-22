from rest_framework.routers import DefaultRouter

from apps.todo.views import TodoApiViewSet

router = DefaultRouter()
router.register(
    prefix="",
    viewset=TodoApiViewSet
)

urlpatterns = router.urls
