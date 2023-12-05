from django.urls import reverse

from .test_setup import SetupTest


class HomeTest(SetupTest):
    def test_home(self):
        url = reverse("v1:home:home")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
