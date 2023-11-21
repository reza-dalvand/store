from apps.tests.users.test_setup import SetupTest


class UrlTest(SetupTest):
    def test_urls(self):
        self.assertEqual(self.register_url, "/api/v1/users/register/")
        self.assertEqual(self.login_url, "/api/v1/users/login/")
        self.assertEqual(self.logout_url, "/api/v1/users/logout/")
        self.assertEqual(self.profile_url, "/api/v1/users/profile/1/")
        self.assertEqual(self.change_password_url, "/api/v1/users/change-password/1/")
        self.assertEqual(self.reset_password_url, "/api/v1/users/reset-password/")
        self.assertEqual(
            self.confirm_password_url, "/api/v1/users/reset-password/confirm/"
        )
