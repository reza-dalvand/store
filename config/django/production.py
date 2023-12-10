from pathlib import Path

from config.settings import *

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "store",
        "USER": "root",
        "PASSWORD": "test",
        "HOST": "localhost",  # Or an IP Address that your DB is hosted on
        "PORT": "3306",
    }
}

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

# STATICFILES_DIRS = [
#     BASE_DIR / "assets",
# ]