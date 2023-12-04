import logging
from random import randint

import requests
from django.db import connections
from django.http import HttpResponse
from django.shortcuts import render
from django_redis import get_redis_connection
from Core.services.services import base_view
from Core.tasks import test_task

log = logging.getLogger('Core')


@base_view
def example(request):
    rand_integer = randint(0, 3)
    log.warning(f'TASK SINGLETON STARTED {rand_integer}')
    test_task.delay(rand_integer)

    return render(request, 'Core/example.html')


def health_test(request):
    log.warning('Web Server Alive')
    # Проверка Redis
    if not get_redis_connection("default").flushall():
        log.warning('Redis have not yet come to life')
        return HttpResponse("Redis error", status=500)

    # Проверка базы данных PostgreSQL
    try:
        connections['default'].cursor()
    except Exception as e:
        log.warning(f'Postgres have not yet come to life: {str(e)}')
        return HttpResponse(f"Postgres error: {str(e)}", status=500)

    # Проверка MinIO
    try:
        response = requests.get('http://minio:9000/minio/health/live')
        if response.status_code != 200:
            log.warning(f'MinIO have not yet come to life: status={response.status_code}')
            return HttpResponse(f"MinIO error: Status code {response.status_code}", status=500)
    except Exception as e:
        log.warning(f'MinIO have not yet come to life: {str(e)}')
        return HttpResponse(f"MinIO error: {str(e)}", status=500)

    return HttpResponse("OK")
