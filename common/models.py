import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.fields.current_user import CurrentUserField

user_model = get_user_model()


class BaseModel(models.Model):
    key = models.UUIDField(
        verbose_name=_("UUID"), unique=True, default=uuid.uuid4, editable=False
    )

    owner = CurrentUserField(
        related_name="%(class)s_owner",
        on_delete=models.SET_NULL,
    )

    created_at = models.DateTimeField(
        verbose_name=_("Created at"), auto_now_add=True, editable=False, db_index=True
    )

    modifier = CurrentUserField(
        on_update=True,
        related_name="%(class)s_modifier",
        on_delete=models.SET_NULL,
    )

    updated_at = models.DateTimeField(verbose_name=_("Updated at"), auto_now=True)

    class Meta:
        ordering = ["-id"]
        abstract = True
