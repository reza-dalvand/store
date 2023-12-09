import os

from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from config.django import development

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
    path("api/v1/", include("apps.api.urls", namespace="v1")),
    prefix_default_language=False,
)
