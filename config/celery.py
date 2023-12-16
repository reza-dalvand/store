import os

from celery import Celery

# imported celery configs into config/django/__init__.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.django")
app = Celery("store")
app.config_from_object("config.celery", namespace="CELERY")

app.autodiscover_tasks()


app.conf.beat_schedule = {
    "example_schedule_task-every-5": {
        "task": "config.tasks.example_schedule_task",
        "schedule": 5.0,
    },
}

app.conf.update(
    task_routes={
        "tasks.send_mail_to_users": "q1",
        "tasks.example_schedule_task": "q2",
    },
    task_annotations={"tasks.example_schedule_task": {"rate_limit": "10/m"}},
    enable_utc=True,
    timezone="UTC",
    broker_connection_retry_on_startup=True,
)
