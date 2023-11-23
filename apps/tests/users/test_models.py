from .test_setup import SetupTest


class ModelTest(SetupTest):
    def test_str_model(self):
        self.assertEquals(str(self.user), self.user.email)
