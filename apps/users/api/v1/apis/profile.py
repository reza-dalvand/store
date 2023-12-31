from rest_framework import generics, status
from rest_framework.response import Response

from apps.users.models import User
from apps.users.serializers import UpdateProfileSerializer


class UserProfileApi(generics.UpdateAPIView):
    """Update User Profile"""

    # renderer_classes = [CustomAesRenderer]

    serializer_class = UpdateProfileSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
