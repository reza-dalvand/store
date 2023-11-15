from django.urls import path, include

app_name = "core"

urlpatterns = [
    path("users/", include("apps.apis.v1.users.urls", namespace="users")),
    path("products/", include("apps.apis.v1.products.urls", namespace="products")),
    path("basket/", include("apps.apis.v1.baskets.urls", namespace="basket")),
    path("contact/", include("apps.apis.v1.contact.urls", namespace="contact")),
    path("home/", include("apps.apis.v1.home.urls", namespace="home")),
]
