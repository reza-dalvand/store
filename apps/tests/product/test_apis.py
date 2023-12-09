from django.urls import reverse

from apps.products.models import ProductCategory

from .test_setup import SetupTest


class ProductTest(SetupTest):
    def test_product_list(self):
        url = reverse("v1:products:product-list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_search_product_with_param(self):
        category = ProductCategory.objects.first()
        url = f'{reverse("v1:products:product-list")}?category={category.slug}'
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_retrieve_product(self):
        url = reverse("v1:products:product-detail", args=[1])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_create_comment(self):
        url = reverse("v1:products:comments")
        comment_info = {
            "product": 1,
            "email": "test@example.com",
            "full_name": "test test",
            "message": "test",
        }
        response = self.client.post(url, comment_info)
        self.assertEquals(response.status_code, 201)
