from django.urls import path, include

app_name = "core"

urlpatterns = [
    # apis version 1
    path("users/api/v1/", include("apps.apis.v1.users.urls", namespace="v1")),
    path("products/api/v1/", include("apps.apis.v1.products.urls", namespace="v1")),
    path("basket/api/v1/", include("apps.apis.v1.baskets.urls", namespace="v1")),
    path("contact/api/v1/", include("apps.apis.v1.contact.urls", namespace="v1")),
    path("home/api/v1/", include("apps.apis.v1.home.urls", namespace="v1")),
    # apis version 2
    path("users/api/v2/", include("apps.apis.v2.users.urls", namespace="v2")),
    path("products/api/v2/", include("apps.apis.v2.products.urls", namespace="v2")),
    path("basket/api/v2/", include("apps.apis.v2.baskets.urls", namespace="v2")),
    path("contact/api/v2/", include("apps.apis.v2.contact.urls", namespace="v2")),
    path("home/api/v2/", include("apps.apis.v2.home.urls", namespace="v2")),
]
