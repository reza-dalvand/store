from rest_framework.routers import DefaultRouter

from .apis.products import ProductViewSet

router = DefaultRouter()
router.register("", ProductViewSet, basename="product")
