from split_settings.tools import include

from config.celery import app as celery_app
from config.env import env

__all__ = ["celery_app"]


include("base.py")
include("secret.py")
include("../celery.py")
include("../settings/aws.py")
include("../settings/email.py")


if "development" in env("DJANGO_ENV"):
    include("development.py")
elif "production" in env("DJANGO_ENV"):
    include("production.py")
