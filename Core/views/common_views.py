import logging

from django.shortcuts import render, redirect, get_object_or_404
from Core.models import User

from Core.services.services import base_view
from Core.tasks import test_task

log = logging.getLogger(__name__)


@base_view
def example(request):
    log.warning('Log')
    log.warning('Log')
    log.warning('Log')
    log.warning('Log')
    test_task.delay('param1', 'param2')
    return render(request, 'Core/example.html')
