from django.urls import reverse
from .test_setup import SetupTest


class ContactTest(SetupTest):
    def test_contact_us(self):
        url = reverse("v1:contact:contact-us")
        message_info = {
            "fullname": "fullname test",
            "email": "example@example.com",
            "subject": "test",
            "message": "test",
        }
        response = self.client.post(url, message_info)
        self.assertEquals(response.status_code, 201)
