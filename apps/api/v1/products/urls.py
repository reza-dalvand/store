from django.urls import path
from rest_framework.routers import DefaultRouter
from .api import ProductViewSet, CommentApiView

app_name = "products"

router = DefaultRouter()
router.register("", ProductViewSet, basename="product")

urlpatterns = [
    path("comments/", CommentApiView.as_view(), name="comments")
] + router.urls
