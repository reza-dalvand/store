from django.urls import path
from rest_framework.routers import DefaultRouter

from .api import BasketDetailViewSet

app_name = "basket"

router = DefaultRouter()
router.register("list", BasketDetailViewSet, basename="order-api")

urlpatterns = [] + router.urls
