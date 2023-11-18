from django.urls import path
from .api import (
    ResetPasswordApiView,
    ChangeForgetPasswordView,
    ChangePasswordApiView,
    UserProfileAPIView,
    RegisterAPIView,
    LoginAPIView,
    LogoutAPIView,
)

app_name = "users"

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("profile/<pk>/", UserProfileAPIView.as_view(), name="profile"),
    path("reset-password/", ResetPasswordApiView.as_view(), name="reset_password"),
    path(
        "change-password/<pk>/",
        ChangePasswordApiView.as_view(),
        name="change_password",
    ),
    path(
        "change-password/<token>/",
        ChangeForgetPasswordView.as_view(),
        name="change_forget_password",
    ),
]
