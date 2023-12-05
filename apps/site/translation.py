from modeltranslation.translator import TranslationOptions, register

from .models import SiteSetting


@register(SiteSetting)
class SiteSettingTranslationOptions(TranslationOptions):
    fields = ("title", "short_description", "description", "address")
