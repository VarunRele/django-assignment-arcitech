"""
URL configuration for assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
# from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Assignment",
        default_version='v1',
        description="Content uploader",
    ),
    public=True,
    authentication_classes=(TokenAuthentication,),
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cms.urls')),
    path('auth/', obtain_auth_token, name='authentication'),
    path('register/', include('user.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('api/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
]
