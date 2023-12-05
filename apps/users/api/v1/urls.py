from django.urls import path

from .apis.change_password import (
    ChangePasswordApiView,
    ConfirmPasswordView,
    ResetPasswordApiView,
)
from .apis.login import LoginAPIView
from .apis.logout import LogoutAPIView
from .apis.profile import UserProfileAPIView
from .apis.register import RegisterAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("profile/<pk>/", UserProfileAPIView.as_view(), name="profile"),
    path(
        "change-password/<pk>/",
        ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    path("reset-password/", ResetPasswordApiView.as_view(), name="reset-password"),
    path(
        "reset-password/confirm/",
        ConfirmPasswordView.as_view(),
        name="confirm-password",
    ),
]
