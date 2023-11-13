import os

from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()
# Include the base settings file
include("base.py")
include("secret_settings.py")

# Include the environment-specific settings file based on the environment
if "development" in os.getenv("DJANGO_ENV"):
    include("development.py")
elif "production" in os.getenv("DJANGO_ENV"):
    include("production.py")
