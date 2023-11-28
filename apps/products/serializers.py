from rest_framework import serializers
from apps.products.models import Product, ProductComment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        exclude = ["created_at"]

    def create(self, validated_data):
        comment = ProductComment.objects.create(**validated_data)
        comment.save()
        return comment


class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Product
        exclude = ["created_at", "updated_at"]
