from django.urls import path

from .apis.change_password import ChangePasswordApi, ConfirmPasswApi, ResetPasswordApi
from .apis.login import LoginApi
from .apis.logout import LogoutApi
from .apis.profile import UserProfileApi
from .apis.register import RegisterApi

urlpatterns = [
    path("register/", RegisterApi.as_view(), name="register"),
    path("login/", LoginApi.as_view(), name="login"),
    path("logout/", LogoutApi.as_view(), name="logout"),
    path("profile/<pk>/", UserProfileApi.as_view(), name="profile"),
    path(
        "change-password/<pk>/",
        ChangePasswordApi.as_view(),
        name="change-password",
    ),
    path("reset-password/", ResetPasswordApi.as_view(), name="reset-password"),
    path(
        "reset-password/confirm/",
        ConfirmPasswApi.as_view(),
        name="confirm-password",
    ),
]
