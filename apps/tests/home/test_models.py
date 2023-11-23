from .test_setup import SetupTest
from apps.models.home.models import MainSlider


#
class ModelTest(SetupTest):
    def test_str_main_slider_model(self):
        slider = MainSlider.objects.first()
        self.assertEquals(str(slider), slider.title)
