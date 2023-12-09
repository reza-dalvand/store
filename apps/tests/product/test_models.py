from apps.products.models import Product

from .test_setup import SetupTest


class ModelTest(SetupTest):
    def test_str_model(self):
        product = Product.objects.first()
        self.assertEquals(str(product), product.name)
