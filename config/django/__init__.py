from split_settings.tools import include

from config.env import env

# Include the base settings file
include("base.py")
include("secret.py")
include("../settings/aws.py")
include("../settings/email.py")

# Include the environment-specific settings file based on the environment
if "development" in env("DJANGO_ENV"):
    include("development.py")
elif "production" in env("DJANGO_ENV"):
    include("production.py")
