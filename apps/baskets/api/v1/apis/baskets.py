import json

from django.conf import settings

import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.baskets.selectors import (
    change_or_add_product_in_user_basket,
    get_or_create_basket,
    remove_product_in_user_basket,
)
from apps.baskets.serializers import BasketDetailSerializer, BasketSerializer
from config.settings.base import ZP_API_REQUEST, ZP_API_STARTPAY, ZP_API_VERIFY


class BasketViewSet(ModelViewSet):
    """manage order of users"""

    serializer_class = BasketSerializer

    def get_queryset(self):
        return get_or_create_basket(self.request.user.id)

    def retrieve(self, request, *args, **kwargs):
        basket = self.queryset
        serializer = BasketSerializer(basket)
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        basket = self.queryset
        serializer = BasketDetailSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        product_id = serializer.validated_data["product"]
        product_count = serializer.validated_data["count"]

        # if product exists change that else create new product in basket
        is_changed = change_or_add_product_in_user_basket(
            basket.id, product_id, product_count
        )
        if is_changed:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        basket = self.queryset
        product_id = kwargs.get("product_id")
        is_delete = remove_product_in_user_basket(basket, product_id)
        if is_delete:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


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
