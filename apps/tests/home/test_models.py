from apps.models.home.models import MainSlider

from .test_setup import SetupTest


#
class ModelTest(SetupTest):
    def test_str_main_slider_model(self):
        slider = MainSlider.objects.first()
        self.assertEquals(str(slider), slider.title)
