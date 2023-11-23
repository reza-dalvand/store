from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory
from apps.models.baskets.models import Basket
from apps.models.products.models import Product
from apps.users.models import User


class SetupTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        product_info = {
            "name": "test",
            "slug": "test",
            "is_published": True,
            "price": 12345,
        }
        Product.objects.create(**product_info).save()
        Basket.objects.create(user_id=1, is_open=True).save()
        return super().setUpTestData

    def setUp(self):
        self.factory = APIRequestFactory()

        self.credentials = {
            "id": "1",
            "email": "test@test.com",
            "username": "test",
            "password": "1234",
        }
        self.user = User.objects.create_user(**self.credentials)
        self.user.save()

        self.token = Token.objects.create(user_id=self.credentials["id"])
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        self.basket = Basket.objects.get(id=1)
        self.basket.details.create(product_id=1, basket_id=1, count=2).save()

        # set user in every request
        self.client.user = self.user
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        print("finished tests of basket app")
        return super().tearDownClass()
