import uuid

from django.utils.translation import gettext_lazy as _

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from apps.users.models import User
from apps.users.serializers import (
    ChangePasswordSerializer,
    ConfirmPasswordSerializer,
    ResetPasswordSerializer,
)
from config.tasks import send_mail_to_users


class ChangePasswordApi(generics.UpdateAPIView):
    """change old password"""

    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer


class ResetPasswordApi(APIView):
    """send reset password email"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        user = User.objects.filter(email__iexact=email).first()
        if user:
            api_version = request.version

            """diagnosis user with uid and api version"""
            callback_url = (
                request.build_absolute_uri(
                    reverse(f"{api_version}:users:confirm-password")
                )
                + f"?uid={user.uid}"
            )
            send_mail_to_users.delay(
                _("change password"), f"click on link {callback_url}", [user.email]
            )
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ConfirmPasswordApi(APIView):
    """confirm reset password"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ConfirmPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_uid = serializer.validated_data["uid"]
        new_password = serializer.validated_data["new_password"]
        confirm_password = serializer.validated_data["confirm_password"]
        if new_password != confirm_password:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(uid__iexact=user_uid).first()
        if user:
            user.set_password(new_password)
            user.uid = uuid.uuid4()
            user.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
