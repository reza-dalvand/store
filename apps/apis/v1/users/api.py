from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import update_last_login
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User
from apps.users.serializers import (
    RegisterSerializer,
    UserProfileSerializer,
    ChangePasswordSerializer,
    ResetPasswordEmailSerializer,
    ChangeForgetPasswordSerializer,
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
        token, created = Token.objects.get_or_create(user=user)
        return Response({"status": status.HTTP_200_OK, "Token": token.key})


class LogoutAPIView(LoginRequiredMixin, APIView):
    """logout user"""

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({"logout": "Successful"}, status=status.HTTP_200_OK)


class UserProfileView(generics.UpdateAPIView):
    """update user profile"""

    serializer_class = UserProfileSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_200_OK)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):
    """change password in user profile"""

    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer


class ResetPasswordView(APIView):
    """send reset password email"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ResetPasswordEmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get("email")
            user = User.objects.filter(email__iexact=email).first()
            # url = f'http://127.0.0.1:8000/auth/api/change-password/{user.token}'
            # send_mail_to_users(_("change password"), f'click on link {url}', [user.email])
            return Response(status.HTTP_200_OK)


class ChangeForgetPasswordView(APIView):
    """change password"""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ChangeForgetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user_token = kwargs.get("token")
            new_password = serializer.data.get("new_password")
            confirm_password = serializer.data.get("confirm_password")
            user: User = User.objects.filter(token__iexact=user_token).first()
            if user and new_password == confirm_password:
                user.set_password(new_password)
                user.token = uuid.uuid4()
                user.save()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
