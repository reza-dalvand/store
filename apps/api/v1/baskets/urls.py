from django.urls import path
from rest_framework.routers import DefaultRouter

from .api import BasketDetailViewSet

app_name = "basket"

router = DefaultRouter()
router.register("", BasketDetailViewSet, basename="basket")

urlpatterns = [] + router.urls
