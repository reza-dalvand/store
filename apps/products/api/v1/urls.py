from django.urls import path

from .routers import router
from .apis.comments import CommentApiView


urlpatterns = [
    path("comments/", CommentApiView.as_view(), name="comments")
] + router.urls
