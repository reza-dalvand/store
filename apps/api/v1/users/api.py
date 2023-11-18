from django.contrib.auth.models import update_last_login
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from scripts.mail import send_mail_to_users
from rest_framework import status, generics
from apps.users.models import User
from apps.users.serializers import (
    RegisterSerializer,
    UpdateProfileSerializer,
    ChangePasswordSerializer,
    ResetPasswordSerializer,
    ConfirmPasswordSerializer,
    LoginSerializer,
)
import uuid


class RegisterAPIView(generics.GenericAPIView):
    """Registers user"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user).key
        return Response({"token": token}, status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    """login user"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        update_last_login(None, user)
        token, created = Token.objects.get_or_create(user=user).key
        return Response({"status": status.HTTP_200_OK, "Token": token})


class LogoutAPIView(APIView):
    """logout user"""

    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({"Logged out": "successfully"}, status=status.HTTP_200_OK)


class UserProfileAPIView(generics.UpdateAPIView):
    """User Profile"""

    serializer_class = UpdateProfileSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangePasswordApiView(generics.UpdateAPIView):
    """change old password"""

    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer


class ResetPasswordApiView(APIView):
    """send reset password email"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        user = User.objects.filter(email__iexact=email).first()
        if user:
            api_version = request.version

            "" "diagnosis user with uid and api version" ""
            callback_url = (
                request.build_absolute_uri(
                    reverse(f"{api_version}:users:confirm-password")
                )
                + f"?uid={user.uid}"
            )
            send_mail_to_users(
                _("change password"), f"click on link {callback_url}", [user.email]
            )
            return Response(status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ConfirmPasswordView(APIView):
    """confirm reset password"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ConfirmPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_uid = serializer.validated_data["uid"]
        new_password = serializer.validated_data["new_password"]
        user: User = User.objects.filter(uid__iexact=user_uid).first()
        if user:
            user.set_password(new_password)
            user.uid = uuid.uuid4()
            user.save()
            return Response(status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
