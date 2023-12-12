from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import ValidationError

mobile_regex = RegexValidator(
    regex=r"(+98 | 0 | 98)9(0[1 - 5] | [1 3]\d | 2[0 - 2] | 98)\d{7}",
    message=_("Phone number must be begin with +98 and 11 digits"),
)


def validate_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError(_("This field accepts mail id of google only"))
