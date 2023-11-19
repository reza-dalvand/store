from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models.products.models import Product, ProductComment
from apps.serializers import ProductSerializer, CommentSerializer


class ProductViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        products = Product.objects.select_related("category", "brand").filter(
            is_published=True, soft_deleted=False
        )
        category = request.query_params.get("category")
        brand = request.query_params.get("brand")
        """filter product by category or brand"""
        if category or brand:
            products = products.filter(
                Q(brand__slug__exact=brand) | Q(category__slug__exact=category),
                is_published=True,
                soft_deleted=False,
            )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def create(self, validated_data):
        product = Product.objects.get(id=validated_data["product_id"])
        if not ProductComment.objects.filter(email=validated_data["email"]).exists():
            comment = ProductComment.objects.create(product=product, **validated_data)
            comment.save()
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response("Forbidden", status.HTTP_403_FORBIDDEN)

    def retrieve(self, pk=None):
        queryset = Product.objects.filter(is_published=True, soft_deleted=False)
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
