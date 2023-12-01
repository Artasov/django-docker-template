from celery import shared_task

from config.celery_conf import app


@app.task()
def test_task(param1, param2):
    print(f"{param1} SUCCESS {param2}")
    return f"{param1} SUCCESS {param2}"


@app.task()
def test_periodic_task(param1, param2):
    print(f"{param1} SUCCESS {param2}")
    return f"{param1} SUCCESS {param2}"
