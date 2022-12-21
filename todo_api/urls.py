from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Todo API')

api_urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('todo/', include('apps.todo.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),

    # swagger
    path('swagger/', schema_view),
    
    # api
    path('', include(api_urlpatterns))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
