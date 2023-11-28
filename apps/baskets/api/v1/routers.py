from rest_framework.routers import DefaultRouter
from .apis.baskets import BasketViewSet

router = DefaultRouter()
router.register("", BasketViewSet, basename="basket")
