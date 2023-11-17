import json

import requests
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.models.baskets.models import Basket, BasketDetail
from apps.serializers import BasketSerializer, BasketDetailSerializer


class BasketDetailViewSet(ModelViewSet):
    """manage orders of user"""

    serializer_class = BasketSerializer
    queryset = BasketDetail.objects.all()

    def list(self, request, *args, **kwargs):
        basket, created = Basket.objects.get_or_create(
            user_id=self.request.user.id, is_open=True
        )
        serializer = BasketSerializer(basket)
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        basket, created = Basket.objects.prefetch_related("details").get_or_create(
            user_id=self.request.user.id, is_open=True
        )

        serializer = BasketDetailSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            detail_product_in_basket = basket.details.filter(
                product=request.POST.get("product_id")
            ).first()
            if detail_product_in_basket:
                detail_product_in_basket.count += int(request.POST.get("count"))
                detail_product_in_basket.save()
                return Response(status.HTTP_201_CREATED)
            BasketDetail.objects.create(
                product_id=request.POST.get("product_id"),
                basket_id=basket.id,
                count=request.POST.get("count"),
            )
            return Response(status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        basket, created = Basket.objects.prefetch_related("details").get_or_create(
            user_id=self.request.user.id, is_open=True
        )
        if kwargs.get("pk"):
            basket.details.filter(id=kwargs.get("pk")).delete()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_404_NOT_FOUND)


ZP_API_REQUEST = f"https://www.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://www.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://www.zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = "YOUR_PHONE_NUMBER"  # Optional
# Important: need to edit for realy server.
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
