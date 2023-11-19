import json

import requests
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.models.baskets.models import Basket, BasketDetail
from apps.serializers import BasketSerializer, BasketDetailSerializer
from config.settings.base import ZP_API_REQUEST, ZP_API_STARTPAY, ZP_API_VERIFY


class BasketDetailViewSet(ModelViewSet):
    """manage orders of user"""

    serializer_class = BasketSerializer

    def get_queryset(self):
        basket, created = Basket.objects.prefetch_related("details").get_or_create(
            user_id=self.request.user.id, is_open=True
        )
        return basket

    def list(self, request, *args, **kwargs):
        basket = self.get_queryset()
        serializer = BasketSerializer(basket)
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        basket = self.get_queryset()
        serializer = BasketDetailSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        product = serializer.validated_data["product"]
        product_count = serializer.validated_data["count"]

        """check product exists in basket"""
        product_in_basket = basket.details.filter(product=product).first()
        if product_in_basket:
            product_in_basket.count += product_count
            product_in_basket.save()
            return Response(status.HTTP_200_OK)

        """put product to basket"""
        BasketDetail.objects.create(
            basket_id=basket.id,
            product=product,
            count=product_count,
        )
        return Response(status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        basket = self.get_queryset()
        if kwargs.get("pk"):
            basket.details.filter(id=kwargs.get("pk")).delete()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_404_NOT_FOUND)


amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = "YOUR_PHONE_NUMBER"
CallbackURL = "http://127.0.0.1:8080/verify/"


def send_request(request):
    data = {
        "MerchantID": "1236468796878976",
        "Amount": amount,
        "Description": description,
        "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {"content-type": "application/json", "content-length": str(len(data))}
    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)

        if response.status_code == 200:
            response = response.json()
            if response["Status"] == 100:
                return {
                    "status": True,
                    "url": ZP_API_STARTPAY + str(response["Authority"]),
                    "authority": response["Authority"],
                }
            else:
                return {"status": False, "code": str(response["Status"])}
        return response

    except requests.exceptions.Timeout:
        return {"status": False, "code": "timeout"}
    except requests.exceptions.ConnectionError:
        return {"status": False, "code": "connection error"}


def verify(authority):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Authority": authority,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {"content-type": "application/json", "content-length": str(len(data))}
    response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response["Status"] == 100:
            return {"status": True, "RefID": response["RefID"]}
        else:
            return {"status": False, "code": str(response["Status"])}
    return response
