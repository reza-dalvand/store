from rest_framework import serializers
from apps.models.baskets.models import BasketDetail, Basket


class BasketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketDetail
        exclude = ["create_at", "basket"]


class BasketSerializer(serializers.ModelSerializer):
    details = BasketDetailSerializer(many=True)

    class Meta:
        model = Basket
        fields = ["user", "is_open", "details"]
