from django.urls import path
from rest_framework.routers import DefaultRouter
from .api import ProductApi

app_name = "products"

router = DefaultRouter()
router.register("products", ProductApi, basename="product_api")

urlpatterns = [] + router.urls
