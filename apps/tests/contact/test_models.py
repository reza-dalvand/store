from .test_setup import SetupTest
from ...models.contact.models import ContactUs


class ModelTest(SetupTest):
    def test_str_model(self):
        contact = ContactUs.objects.first()
        self.assertEquals(str(contact), contact.fullname)
