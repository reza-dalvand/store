from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.models.site.models import SiteSetting
from apps.serializers import ContactUsSerializer


class ContactUsView(GenericAPIView):
    serializer_class = ContactUsSerializer

    def get_queryset(self):
        qs = SiteSetting.objects.filter(is_active=True).first()
        return qs

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"contact us": "successful register message"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"contact us": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST
        )
