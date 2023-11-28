from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.products.serializers import CommentSerializer


class CommentApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
