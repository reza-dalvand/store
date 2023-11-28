from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("", include("apps.baskets.urls", "authentication")),
    path("", include("apps.users.urls", "users")),
    path("", include("apps.products.urls", "address")),
    path("", include("apps.contact.urls", "common")),
    path("", include("apps.home.urls", "payment")),
]
