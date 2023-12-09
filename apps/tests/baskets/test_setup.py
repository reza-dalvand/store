from model_bakery import baker
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APITestCase

from apps.baskets.models import Basket, BasketDetail
from apps.products.models import Product
from apps.users.models import User


class SetupTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(Product)
        baker.make(User)
        user = User.objects.first()
        Token.objects.create(user=user)
        Basket.objects.create(user_id=user.id, is_open=True)
        return super().setUpTestData

    def setUp(self):
        self.factory = APIRequestFactory()

        self.token = Token.objects.first()
        self.user = User.objects.first()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        self.basket = Basket.objects.first()
        self.product = Product.objects.first()

        self.basket.details.create(
            product_id=self.product.id, basket_id=self.basket.id
        ).save()

        # set user in every request
        self.client.user = self.user
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        print("finished tests of basket app")
        return super().tearDownClass()
