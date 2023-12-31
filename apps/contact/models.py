from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.common.validators import validate_mail


class ContactUs(BaseModel):
    fullname = models.CharField(_("fullname"), max_length=150)
    email = models.EmailField(_("email"), validators=[validate_mail])
    subject = models.CharField(_("subject"), max_length=300)
    message = models.TextField(_("message"))
    date = models.DateTimeField(_("date"), auto_now_add=True)
    is_read = models.BooleanField(_("read / unread"), default=False)

    class Meta:
        verbose_name = _("Contact Us")
        verbose_name_plural = _("Contact Us")

    def __str__(self):
        return self.fullname
