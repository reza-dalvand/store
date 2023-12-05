from modeltranslation.translator import TranslationOptions, register

from .models import MainSlider


@register(MainSlider)
class MainSliderTranslationOptions(TranslationOptions):
    fields = ("title",)
