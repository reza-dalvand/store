from .test_setup import SetupTest
from apps.models.products.models import Product


class ModelTest(SetupTest):
    def test_str_model(self):
        product = Product.objects.first()
        self.assertEquals(str(product), product.name)
