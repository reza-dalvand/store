from django.db import models
from common.models import BaseModel
from django.utils.translation import gettext_lazy as _


# Create your models here.
class SiteSetting(BaseModel):
    title = models.CharField(max_length=90, verbose_name=_("title"))
    email = models.EmailField(null=True, verbose_name=_("email"))
    short_description = models.TextField(verbose_name=_("short description"))
    description = models.TextField(_("description"))
    address = models.TextField(null=True, verbose_name=_("address"))
    mobile = models.CharField(null=True, max_length=11, verbose_name=_("mobile"))
    phone_number = models.CharField(
        null=True, max_length=11, verbose_name=_("phone number")
    )
    is_active = models.BooleanField(default=False, verbose_name=_("is active"))

    class Meta:
        verbose_name = _("تنظیمات سایت")
        verbose_name_plural = _("Site Settings")

    def __str__(self):
        return self.title
