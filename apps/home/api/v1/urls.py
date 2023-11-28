from django.urls import path

from .apis.home import Home

urlpatterns = [
    path("", Home.as_view(), name="home"),
]
