from time import sleep

from config.celery import app


@app.task()
def notify_customers():
    sleep(10)
    print("example test")
