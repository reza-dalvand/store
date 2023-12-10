from pathlib import Path

import environ

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env.read_env(BASE_DIR / ".env")

ARVAN_STORAGE_URL = env("ARVAN_STORAGE_URL")
# Arvan Cloud Storage

if env("USE_ARVAN_BUCKET", cast=bool, default=False):
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
ARVAN_ACCESS_KEY_ID = env("ARVAN_ACCESS_KEY_ID", cast=str)
ARVAN_SECRET_ACCESS_KEY = env("ARVAN_SECRET_ACCESS_KEY", cast=str)
ARVAN_ENDPOINT_URL = env("ARVAN_ENDPOINT_URL", cast=str)
ARVAN_STORAGE_BUCKET_NAME = env("ARVAN_STORAGE_BUCKET_NAME", cast=str)
ARVAN_STORAGE_REGION_NAME = env("ARVAN_STORAGE_REGION_NAME", cast=str)
AWS_SERVICE_NAME = "s3"
AWS_S3_FILE_OVERWRITE = False
ARVAN_STORAGE_DEFAULT_ACL = env("ARVAN_STORAGE_DEFAULT_ACL", cast=str)
AWS_LOCAL_STORAGE = f"{BASE_DIR}/media_files/aws/"
AWS_QUERYSTRING_AUTH = env("AWS_QUERYSTRING_AUTH", cast=bool)
