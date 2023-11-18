from django.urls import path
from rest_framework.routers import DefaultRouter
from .api import ProductViewSet, CommentApiView

app_name = "products"

router = DefaultRouter()
router.register("", ProductViewSet, basename="product-api")

urlpatterns = [
    path("comment/", CommentApiView.as_view(), name="comments")
] + router.urls
