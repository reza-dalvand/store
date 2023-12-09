from apps.contact.models import ContactUs

from .test_setup import SetupTest


class ModelTest(SetupTest):
    def test_str_model(self):
        contact = ContactUs.objects.first()
        self.assertEquals(str(contact), contact.fullname)
