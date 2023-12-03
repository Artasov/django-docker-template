import logging
from time import sleep

from celery import shared_task
from celery_singleton import Singleton

from Core.services.services import base_view
from config.celery_conf import app

log = logging.getLogger('Core task')


@app.task(base=Singleton, unique_on=['rand_integer', ])
def test_task(rand_integer):
    sleep(5)
    log.warning(f"TASK SINGLETON SUCCESS {rand_integer}")


@shared_task
@base_view
def test_periodic_task(param1):
    log.warning(f"TASK PERIODIC SUCCESS {param1}")
