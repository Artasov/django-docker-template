import logging
from random import randint
from django.shortcuts import render
from django_redis import get_redis_connection
from Core.services.services import base_view
from Core.tasks import test_task

log = logging.getLogger('Core')


@base_view
def example(request):
    log.warning(f'Redis cache available! {get_redis_connection("default").flushall()}')

    rand_integer = randint(0, 3)
    log.warning(f'TASK SINGLETON STARTED {rand_integer}')
    test_task.delay(rand_integer)

    return render(request, 'Core/example.html')
