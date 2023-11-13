from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

# STATICFILES_DIRS = [
#     BASE_DIR / "assets",
# ]


# MEDIA_URL = "/media/"
# MEDIA_ROOT = BASE_DIR / "media"
