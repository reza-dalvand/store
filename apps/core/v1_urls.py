from django.urls import path, include

app_name = "core"

urlpatterns = [
    path("users/", include("apps.api.v1.users.urls", namespace="users")),
    path("products/", include("apps.api.v1.products.urls", namespace="products")),
    path("basket/", include("apps.api.v1.baskets.urls", namespace="basket")),
    path("contact/", include("apps.api.v1.contact.urls", namespace="contact")),
    path("home/", include("apps.api.v1.home.urls", namespace="home")),
]
