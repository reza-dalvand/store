from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("baskets/", include("apps.baskets.urls", "baskets")),
    path("users/", include("apps.users.urls", "users")),
    path("products/", include("apps.products.urls", "products")),
    path("contact/", include("apps.contact.urls", "contact")),
    path("home/", include("apps.home.urls", "home")),
]
