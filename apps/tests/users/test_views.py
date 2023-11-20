from model_bakery import baker

from apps.serializers import LoginSerializer, RegisterSerializer
from apps.tests.users.test_setup import SetupTest
from apps.users.models import User


class RegisterTest(SetupTest):
    def setUp(self):
        self.credentials = {
            "email": "test@test.com",
            "username": "test",
            "password": "1234",
            "password2": "1234",
        }
        return super(RegisterTest, self).setUp()

    def test_register(self):
        response = self.client.post(self.register_url, self.credentials)
        self.assertEquals(response.status_code, 201)

    def test_register_serializer(self):
        """used baker model for fill fields"""
        serializer = RegisterSerializer(data=self.credentials)
        self.assertTrue(serializer.is_valid())
        user = User.objects.create_user(baker.make(User))
        self.assertIsNotNone(user)


class LoginTest(SetupTest):
    def setUp(self):
        self.credentials = {
            "email": "login@test.com",
            "username": "test",
            "password": "1234",
        }
        User.objects.create_user(**self.credentials)
        return super(LoginTest, self).setUp()

    def test_login(self):
        response = self.client.post(self.login_url, self.credentials)
        self.assertEquals(response.status_code, 200)

    def test_login_serializer(self):
        serializer = LoginSerializer(data=self.credentials)
        self.assertTrue(serializer.is_valid())
