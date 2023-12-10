from config.env import env

CELERY_BROKER = env("CELERY_BROKER")
CELERY_BACKEND = env("CELERY_BACKEND")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")
CELERY_CACHE_BACKEND = True
CELERY_BROKER_URL = env("CELERY_CACHE_BACKEND")
CELERY_RESULT_EXTENDED = env("CELERY_BROKER_URL")
CELERY_ACCEPT_CONTENT = env("CELERY_RESULT_EXTENDED")
CELERY_TASK_SERIALIZER = env("CELERY_ACCEPT_CONTENT")
CELERY_RESULT_SERIALIZER = env("CELERY_TASK_SERIALIZER")


CELERY_BROKER_BACKEND = "memory"
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True
