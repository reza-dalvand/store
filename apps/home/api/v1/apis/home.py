from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.home.models import MainSlider
from apps.products.models import ProductCategory, Product, ProductBrand
from apps.home.serializers import HomeSerializer


class Home(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        latest_products = Product.objects.filter(
            is_published=True, soft_deleted=False
        ).order_by("-created_at")
        categories = ProductCategory.objects.all()
        brands = ProductBrand.objects.all()
        slides = MainSlider.objects.all()
        data = {
            "products": latest_products,
            "categories": categories,
            "brands": brands,
            "slides": slides,
        }
        serializer = HomeSerializer(data)

        return Response(serializer.data, status=status.HTTP_200_OK)
