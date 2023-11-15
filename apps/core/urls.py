from django.urls import path, include

app_name = "core"

urlpatterns = [
    path("api/v1/", include("apps.apis.v1.users.urls", namespace="v1")),
    path("api/v2/", include("apps.apis.v2.users.urls", namespace="v2")),
]
