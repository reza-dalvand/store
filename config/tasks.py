from time import sleep

from celery import shared_task


@shared_task
def notify_customers():
    print("how are fucking cus")
    sleep(10)
