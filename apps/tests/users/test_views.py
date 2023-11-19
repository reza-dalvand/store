from django.test import TestCase
from django.urls import reverse
from apps.serializers import LoginSerializer, RegisterSerializer
from apps.users.models import User


class LoginTest(TestCase):
    def setUp(self):
        self.url = reverse("v1:users:login")
        self.credentials = {
            "email": "test@test.com",
            "username": "test_user",
            "password": "test",
        }
        User.objects.create_user(**self.credentials)

    def test_login(self):
        serializer = LoginSerializer(data=self.credentials)
        self.response = self.client.post(self.url, self.credentials, follow=True)
        self.assertTrue(serializer.is_valid())
        self.assertEquals(self.response.status_code, 200)


class RegisterTest(TestCase):
    def setUp(self):
        self.url = reverse("v1:users:register")
        self.credentials = {
            "email": "register2@test.com",
            "username": "register2",
            "password": "test",
            "password2": "test",
        }

    def test_register(self):
        self.response = self.client.post(self.url, self.credentials, follow=True)
        self.assertEquals(self.response.status_code, 201)

    def test_register_serializer(self):
        serializer = RegisterSerializer(data=self.credentials)
        self.assertTrue(serializer.is_valid())
        self.credentials.pop("password2")
        user = User.objects.create_user(**self.credentials)
        self.assertIsNotNone(user)
