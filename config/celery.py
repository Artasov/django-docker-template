from celery import Celery

app = Celery('config')

import os

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_connection_retry_on_startup = True

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
