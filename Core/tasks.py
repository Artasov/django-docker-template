import logging
from time import sleep

from celery import shared_task
from celery_singleton import Singleton

log = logging.getLogger('Core task')


@shared_task(base=Singleton)
def test_task(param1, param2):
    log.warning('TASK SINGLETON STARTED')
    sleep(2)
    log.warning(f"TASK SINGLETON SUCCESS {param1} {param1}")


@shared_task
def test_periodic_task(param1, param2):
    log.warning(f"TASK PERIODIC SUCCESS {param1} {param1}")
