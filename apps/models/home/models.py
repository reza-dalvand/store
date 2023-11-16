from django.db import models
from apps.core.models import BaseModel
from django.utils.translation import gettext_lazy as _


class MainSlider(BaseModel):
    title = models.CharField(_("title"), max_length=255)
    slug = models.SlugField(_("slug"), max_length=255, null=True, blank=True)
    description = models.TextField(_("desc"), null=True, blank=True)
    image = models.ImageField(_("image"), upload_to="slider")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Main Slider")
        verbose_name_plural = _("Main Sliders")

    def __str__(self):
        return self.title
