# -*- coding: utf-8 -*-

from flask import Flask
from celery import Celery

app = Flask(__name__)

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def my_background_task(arg1, arg2):
    # some long running task here
    return result

# task = my_background_task.delay(10, 20)
task = my_background_task.apply_async(args=[10, 20], countdown=60)