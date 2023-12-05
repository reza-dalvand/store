from model_bakery import baker

from apps.serializers import LoginSerializer, RegisterSerializer
from apps.users.models import User

from .test_setup import SetupTest


class RegisterTest(SetupTest):
    def setUp(self):
        self.credentials_register = {
            "email": "register@test.com",
            "username": "register",
            "password": "1234",
            "password2": "1234",
        }
        return super(RegisterTest, self).setUp()

    def test_register_valid(self):
        response = self.client.post(self.register_url, self.credentials_register)
        self.assertEquals(response.status_code, 201)

    def test_register_invalid(self):
        self.credentials_register["email"] = "invalid data"
        response = self.client.post(self.register_url, self.credentials_register)
        self.assertEquals(response.status_code, 400)

    def test_register_serializer_valid(self):
        """used baker model for fill fields"""
        serializer = RegisterSerializer(data=self.credentials_register)
        self.assertTrue(serializer.is_valid())
        user = User.objects.create_user(baker.make(User))
        self.assertIsNotNone(user)

    def test_register_serializer_invalid(self):
        self.credentials_register["email"] = "invalid data"
        serializer = RegisterSerializer(data=self.credentials_register)
        self.assertFalse(serializer.is_valid())


class LoginTest(SetupTest):
    def test_login(self):
        response = self.client.post(self.login_url, self.credentials)
        self.assertEquals(response.status_code, 200)

    def test_login_invalid(self):
        self.credentials["email"] = "invalid data"
        response = self.client.post(self.login_url, self.credentials)
        self.assertEquals(response.status_code, 400)

    def test_login_serializer_valid(self):
        serializer = LoginSerializer(data=self.credentials)
        self.assertTrue(serializer.is_valid())

    def test_login_serializer_invalid(self):
        self.credentials["email"] = "invalid data"
        serializer = LoginSerializer(data=self.credentials)
        self.assertFalse(serializer.is_valid())


class LogoutTest(SetupTest):
    def test_logout(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code, 200)


class ProfileTest(SetupTest):
    def setUp(self):
        self.data = {
            "old_password": "1234",
            "new_password": "Test1234!",
            "confirm_password": "Test1234!",
        }
        return super().setUp()

    def test_get_profile(self):
        response = self.client.get(self.profile_url)
        self.assertEquals(response.data["username"], self.user.username)
        self.assertEquals(response.status_code, 200)

    def test_update_profile_valid(self):
        response = self.client.put(self.profile_url, self.credentials)
        self.assertEquals(response.status_code, 200)

    def test_update_profile_invalid(self):
        self.credentials["email"] = "invalid data"
        response = self.client.put(self.profile_url, self.credentials)
        self.assertEquals(response.status_code, 400)

    def test_change_old_password_valid(self):
        response = self.client.put(self.change_password_url, self.data)
        self.assertEquals(response.status_code, 200)

    def test_change_password_with_invalid_old_pass(self):
        self.data["old_password"] = "incorrect password"
        response = self.client.put(self.change_password_url, self.data)
        self.assertEquals(response.status_code, 400)

    def test_change_password_with_passwords_not_match(self):
        self.data["new_password"] = "incorrect password"
        response = self.client.put(self.change_password_url, self.data)
        self.assertEquals(response.status_code, 400)


class ResetPassword(SetupTest):
    def setUp(self):
        super().setUp()
        self.data = {
            "new_password": "Test12345!",
            "confirm_password": "Test12345!",
            "uid": self.user.uid,
        }

    def test_send_reset_password_mail(self):
        response = self.client.post(
            self.reset_password_url, data={"email": self.credentials["email"]}
        )
        self.assertEquals(response.status_code, 200)

    def test_send_reset_password_mail_invalid(self):
        response = self.client.post(
            self.reset_password_url, data={"email": "invalid email"}
        )
        self.assertEquals(response.status_code, 400)

    def test_confirm_reset_password(self):
        response = self.client.post(self.confirm_password_url, self.data)
        self.assertEquals(response.status_code, 200)

    def test_confirm_reset_password_invalid_uid(self):
        self.data["uid"] = "invalid uid"
        response = self.client.post(self.confirm_password_url, self.data)
        self.assertEquals(response.status_code, 404)

    def test_confirm_reset_password_invalid(self):
        self.data["confirm_password"] = "invalid confirm password"
        response = self.client.post(self.confirm_password_url, self.data)
        self.assertEquals(response.status_code, 400)
