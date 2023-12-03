import logging

from django.core.cache import cache
from django.shortcuts import render, redirect, get_object_or_404
from Core.models import User

from Core.services.services import base_view
from Core.tasks import test_task

log = logging.getLogger('Core')


@base_view
def example(request):
    log.warning('example_log')
    cashing_data_name = 'cashing_data'
    cashing_data = {'abc': 123, 'cba':321}
    if cache.get(cashing_data_name):
        log.warning('cache found')
    else:
        cache.set(cashing_data_name, cashing_data, 10)
    test_task.delay('param1', 'param2')
    return render(request, 'Core/example.html')
