from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.serializers.contact.serializers import ContactUsSerializer


class ContactUsView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactUsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
