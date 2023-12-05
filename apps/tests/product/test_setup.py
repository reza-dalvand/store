from model_bakery import baker
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APITestCase

from apps.models.products.models import Product, ProductBrand, ProductCategory
from apps.users.models import User


class SetupTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(ProductCategory).save()
        baker.make(ProductBrand).save()
        baker.make(Product, category_id=1, brand_id=1, is_published=True).save()
        baker.make(User).save()
        Token.objects.create(user_id=1)

        return super().setUpTestData

    def setUp(self):
        self.factory = APIRequestFactory()
        self.token = Token.objects.first()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        # set user into every request
        self.client.user = User.objects.first()
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        print("finished tests of product app")
        return super().tearDownClass()
