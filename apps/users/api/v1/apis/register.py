from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.serializers import RegisterSerializer


class RegisterApi(generics.GenericAPIView):
    """Registers user"""

    permission_classes = [AllowAny]
    # renderer_classes = [CustomAesRenderer]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user).key
        return Response({"token": token}, status.HTTP_201_CREATED)
