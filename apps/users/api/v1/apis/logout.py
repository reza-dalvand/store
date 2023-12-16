from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView


class LogoutApi(APIView):
    """logout user"""

    # renderer_classes = [CustomAesRenderer]

    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({"Logged out": "successfully"}, status=status.HTTP_200_OK)
