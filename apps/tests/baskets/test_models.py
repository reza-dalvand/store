from .test_setup import SetupTest


class ModelTest(SetupTest):
    def test_str_model(self):
        print("Model")
        self.assertEquals(str(self.basket), self.basket.user.get_full_name())
