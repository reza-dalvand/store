from rest_framework.routers import DefaultRouter
from .api import BasketViewSet

app_name = "basket"

router = DefaultRouter()
router.register("", BasketViewSet, basename="basket")

urlpatterns = [] + router.urls
