from rest_framework import serializers
from apps.home.models import MainSlider
from apps.products.models import ProductBrand, Product, ProductCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = "__all__"


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSlider
        fields = "__all__"


class HomeSerializer(serializers.Serializer):
    categories = CategorySerializer(many=True)
    brands = BrandSerializer(many=True)
    products = ProductSerializer(many=True)
    slides = SliderSerializer(many=True)
