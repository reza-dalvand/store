from django.urls import reverse

from model_bakery import baker

from apps.baskets.models import BasketDetail

from .test_setup import SetupTest


class BasketTest(SetupTest):
    def setUp(self):
        super().setUp()
        self.basket_detail = {
            "product": self.product.id,
            "count": 1,
            "final_price": 9999,
        }

    def test_create_basket(self):
        url = reverse("v1:basket:basket-list")
        response = self.client.post(url, self.basket_detail)
        self.assertIn(response.status_code, [201, 200])

    def test_destroy_basket(self):
        url = reverse("v1:basket:basket-detail", args=[1])
        response = self.client.delete(url)
        self.assertIn(response.status_code, [404, 200])
