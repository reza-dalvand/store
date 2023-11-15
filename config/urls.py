"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import os

from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from config.settings import development

schema_view = get_schema_view(
    openapi.Info(title="Document of Apis", default_version="v1"),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
]

urlpatterns += static(development.STATIC_URL, document_root=development.STATIC_ROOT)
if "development" in os.getenv("DJANGO_ENV"):
    urlpatterns += static(development.MEDIA_URL, document_root=development.MEDIA_ROOT)
    urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("rosetta/", include("rosetta.urls")),
    path("", include("apps.core.urls", namespace="apps")),
    prefix_default_language=None,
)
