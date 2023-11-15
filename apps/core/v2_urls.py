from django.urls import path, include

app_name = "core"

urlpatterns = [
    path("users/", include("apps.apis.v2.users.urls", namespace="users")),
    path("products/", include("apps.apis.v2.products.urls", namespace="products")),
    path("basket/", include("apps.apis.v2.baskets.urls", namespace="basket")),
    path("contact/", include("apps.apis.v2.contact.urls", namespace="contact")),
    path("home/", include("apps.apis.v2.home.urls", namespace="home")),
]
