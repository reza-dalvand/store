from django.urls import path

from .apis.comments import CommentApiView
from .routers import router

urlpatterns = [
    path("comments/", CommentApiView.as_view(), name="comments")
] + router.urls
