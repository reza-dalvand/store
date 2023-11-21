from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory
from apps.users.models import User
from django.urls import reverse


class SetupTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        return super().setUpTestData

    def setUp(self):
        self.factory = APIRequestFactory()
        """views url"""
        self.register_url = reverse("v1:users:register")
        self.login_url = reverse("v1:users:login")
        self.logout_url = reverse("v1:users:logout")
        self.profile_url = reverse("v1:users:profile", args=[1])
        self.change_password_url = reverse("v1:users:change-password", args=[1])
        self.reset_password_url = reverse("v1:users:reset-password")
        self.confirm_password_url = reverse("v1:users:confirm-password")

        self.credentials = {
            "id": 1,
            "email": "test@test.com",
            "username": "test",
            "first_name": "test",
            "last_name": "test",
            "phone_number": "12345678912",
            "password": "1234",
        }

        self.user = User.objects.create_user(**self.credentials)
        self.user.save()
        self.token = Token.objects.create(user_id=self.credentials["id"])
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        """set user into every request"""
        self.client.user = self.user

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()
