from django.urls import path

from .api import Home

app_name = "home"
urlpatterns = [
    path("", Home.as_view(), name="home"),
]
