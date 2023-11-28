from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics


class LogoutAPIView(APIView):
    """logout user"""

    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({"Logged out": "successfully"}, status=status.HTTP_200_OK)
