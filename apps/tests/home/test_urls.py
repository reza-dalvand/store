from django.urls import reverse

from .test_setup import SetupTest


class UrlTest(SetupTest):
    def test_urls(self):
        self.assertEqual(reverse("v1:home:home"), "/api/v1/home/")
