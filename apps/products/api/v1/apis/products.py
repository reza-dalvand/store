from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.products.selectors import get_active_products
from apps.products.serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        category = request.query_params.get("category")
        brand = request.query_params.get("brand")
        # get active products or filter by category or brand
        qs = get_active_products(category, brand)
        serializer = ProductSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        qs = get_active_products()
        product = get_object_or_404(qs, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
