from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse
from model_bakery import baker
from apps.users.models import User


class SetupTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.login_url = reverse("v1:users:login")
        self.register_url = reverse("v1:users:register")
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
