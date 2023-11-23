from model_bakery import baker
from rest_framework.test import APITestCase

from apps.models.contact.models import ContactUs


class SetupTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make(ContactUs)
        return super().setUpTestData

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        print("finished tests of contact app")
        return super().tearDownClass()
