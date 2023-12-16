from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.contact.serializers import ContactUsSerializer


class ContactUsView(APIView):
    permission_classes = [AllowAny]
    # renderer_classes = [CustomAesRenderer]

    def post(self, request, *args, **kwargs):
        serializer = ContactUsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
