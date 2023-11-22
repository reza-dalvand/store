from apps.tests.baskets.test_setup import SetupTest


class ModelTest(SetupTest):
    def test_str_basket_model(self):
        self.assertEquals(str(self.basket), self.basket.user.get_full_name())
