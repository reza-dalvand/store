import time

from django.core.mail import send_mail

from celery import shared_task

from config.celery import app
from config.settings import email


@app.task()
def send_mail_to_users(subject, message, recipient_list):
    email_from = email.EMAIL_HOST_USER
    send_mail(subject, message, email_from, recipient_list)


@app.task()
def example_schedule_task():
    time.sleep(5)
    print("example task")
    return "example task"
