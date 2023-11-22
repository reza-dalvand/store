from django.urls import reverse
from apps.tests.baskets.test_setup import SetupTest


class BasketTest(SetupTest):
    def setUp(self):
        self.basket_detail = {"product": 1, "count": 1, "final_price": 12545}
        return super().setUp()

    def test_list_basket(self):
        url = reverse("v1:basket:basket-list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_create_basket(self):
        url = reverse("v1:basket:basket-list")
        self.basket.delete()
        response = self.client.post(url, self.basket_detail)
        self.assertEquals(response.status_code, 201)

    def test_update_basket(self):
        url = reverse("v1:basket:basket-list")
        response = self.client.post(url, self.basket_detail)
        self.assertEquals(response.status_code, 200)

    def test_destroy_detail_basket(self):
        url = reverse("v1:basket:basket-detail", args=[1])
        response = self.client.delete(url)
        self.assertEquals(response.status_code, 204)

    def test_destroy_with_invalid_data(self):
        url = reverse("v1:basket:basket-detail", args=[1])
        self.basket.details.filter(product_id=1).delete()
        response = self.client.delete(url)
        self.assertEquals(response.status_code, 404)
