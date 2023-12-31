from pathlib import Path

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
