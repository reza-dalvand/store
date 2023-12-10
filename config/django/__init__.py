from split_settings.tools import include

from config.env import env

include("base.py")
include("secret.py")
include("../celery.py")
include("../settings/aws.py")
include("../settings/email.py")

if "development" in env("DJANGO_ENV"):
    include("development.py")
elif "production" in env("DJANGO_ENV"):
    include("production.py")
