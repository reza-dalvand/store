from django.urls import path
from .api import (
    ResetPasswordView,
    ChangeForgetPasswordView,
    ChangePasswordView,
    UserProfileView,
)

app_name = "users"

urlpatterns = [
    path("reset-password/", ResetPasswordView.as_view(), name="reset_password"),
    path(
        "change-password/<token>/",
        ChangeForgetPasswordView.as_view(),
        name="change_password",
    ),
    path(
        "change-password/<int:pk>/",
        ChangePasswordView.as_view(),
        name="api_change_password",
    ),
    path("profile/<pk>/", UserProfileView.as_view(), name="api_user_profile"),
]
