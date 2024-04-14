"""todo_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# from rest_framework import routers, permissions

# from api_wordpress.urls import router as todo_router

from api_wordpress.views import  upload_file
import private_storage.urls # type: ignore

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Todo API",
#       default_version='v1',
#       description="This API is used to manage todos",
#       contact=openapi.Contact(email="contact@simpletech.com"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=False,
#    permission_classes=[permissions.AllowAny],
# )


# router = routers.DefaultRouter()
# router.registry.extend(todo_router.registry)

urlpatterns = [
    path('upload/<extension>/', upload_file),
    # path('convert-to-pdf/<int:file_id>/', convert_to_pdf, name='convert_to_pdf'),

    # path('convert/', FileConvertView.as_view(), name='file-convert'),
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('', include(router.urls)),
    re_path('^private-media/', include(private_storage.urls)),
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
