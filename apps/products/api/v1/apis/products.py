from django.db.models import Q

from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        products = Product.objects.select_related("category", "brand").filter(
            is_published=True, soft_deleted=False
        )
        category = request.query_params.get("category")
        brand = request.query_params.get("brand")
        # filter product by category or brand
        if category or brand:
            products = products.filter(
                Q(brand__slug__exact=brand) | Q(category__slug__exact=category),
                is_published=True,
                soft_deleted=False,
            )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.filter(is_published=True, soft_deleted=False)
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
