import logging
import os
from datetime import timedelta
from pathlib import Path
from typing import List, Tuple

from config import default_settings as dsettings

env_get = os.environ.get

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env_get('SECRET_KEY') or '*'
DEBUG = bool(int(env_get('DEBUG') or 0))
DEV = bool(int(env_get('DEV') or 0))
SITE_ID = int(env_get('SITE_ID') or 1)
WSGI_APPLICATION = 'config.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
HTTPS = bool(int(env_get('HTTPS') or 0))
MAIN_DOMAIN = str(env_get('MAIN_DOMAIN') or 'localhost')
ALLOWED_HOSTS = str((env_get('ALLOWED_HOSTS') or '') + f',{MAIN_DOMAIN}').split(',')
ROOT_URLCONF = 'Core.urls'
AUTH_USER_MODEL = 'Core.User'

REDIS_URL = env_get('REDIS_URL') or 'redis://redis:6379/0'
REDIS_CACHE_URL = env_get('REDIS_CACHE_URL') or 'redis://redis:6379/1'
CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = env_get('TZ') or 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = f'http{"s" if HTTPS else ""}://{MAIN_DOMAIN}/static/'
MEDIA_URL = f'http{"s" if HTTPS else ""}://{MAIN_DOMAIN}/media/'

MINIO_ENDPOINT = 'minio:9000'
MINIO_EXTERNAL_ENDPOINT = f'{MAIN_DOMAIN}:9000'  # For external access use Docker hostname and MinIO port
MINIO_EXTERNAL_ENDPOINT_USE_HTTPS = bool(int(env_get('MINIO_EXTERNAL_ENDPOINT_USE_HTTPS') or 0))
MINIO_ACCESS_KEY = env_get('MINIO_ACCESS_KEY')
MINIO_SECRET_KEY = env_get('MINIO_SECRET_KEY')
MINIO_USE_HTTPS = bool(int(env_get('MINIO_USE_HTTPS') or 0))
MINIO_URL_EXPIRY_HOURS = timedelta(days=1)
MINIO_CONSISTENCY_CHECK_ON_START = True
MINIO_PRIVATE_BUCKETS = [
    'django-backend-dev-private',
]
MINIO_PUBLIC_BUCKETS = [
    'django-backend-dev-public',
]
MINIO_POLICY_HOOKS: List[Tuple[str, dict]] = []
MINIO_MEDIA_FILES_BUCKET = 'media-files'
MINIO_STATIC_FILES_BUCKET = 'static-files'
MINIO_BUCKET_CHECK_ON_SAVE = True  # Default: True // Creates a cart if it doesn't exist, then saves it
DEFAULT_FILE_STORAGE = 'django_minio_backend.models.MinioBackend'
MINIO_PUBLIC_BUCKETS.append(MINIO_STATIC_FILES_BUCKET)
MINIO_PUBLIC_BUCKETS.append(MINIO_MEDIA_FILES_BUCKET)
MINIO_PUBLIC_BUCKETS.append('files-bucket')

STATICFILES_STORAGE = 'django_minio_backend.models.MinioBackendStatic'
FILE_UPLOAD_MAX_MEMORY_SIZE = 65536

LOCAL_APPS = [
    'Core.apps.CoreConfig',
]

THIRD_APPS = [
    'django_celery_beat',
    'django_minio_backend',
    'cachalot',
]

INSTALLED_APPS = dsettings.DJANGO_APPS + THIRD_APPS + LOCAL_APPS

DATABASES = {
    'default': {
        'ENGINE': env_get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': env_get('SQL_DATABASE_NAME', BASE_DIR / 'db.sqlite3'),
        'USER': env_get('SQL_USER', 'admin'),
        'PASSWORD': env_get('SQL_PASSWORD', 'admin'),
        'HOST': env_get('SQL_HOST', 'localhost'),
        'PORT': env_get('SQL_PORT', '5432'),
    }
}

CACHES = {
    'default': {
        # 'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        "BACKEND": "django_redis.cache.RedisCache",
        'LOCATION': REDIS_CACHE_URL,
        'OPTIONS': {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
        }
    }
}
# In some situations, when Redis is only used for
# cache, you do not want exceptions when Redis is
# down. This is default behavior in the memcached
# backend, and it can be emulated in django-redis.
# For setup memcached like behaviour (ignore
# connection exceptions), you should set
# IGNORE_EXCEPTIONS settings on your cache
# configuration:
DJANGO_REDIS_IGNORE_EXCEPTIONS = True
# Configure as session backend
# Django can by default use any cache backend as session
# backend, and you benefit from that by using django-redis
# as backend for session storage without installing any
# additional backends:
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

DJANGO_REDIS_LOGGER = 'RedisLogger'

MIDDLEWARE = [  # Views cache
                 # 'django.middleware.cache.UpdateCacheMiddleware',
                 # 'django.middleware.cache.FetchFromCacheMiddleware',
             ] + dsettings.MIDDLEWARE + []

TEMPLATES = dsettings.TEMPLATES + [

]

AUTH_PASSWORD_VALIDATORS = dsettings.AUTH_PASSWORD_VALIDATORS + [

]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'base_formatter': {
            'format': '{levelname} {asctime} {module}: {message}',
            'style': '{',
            'encoding': 'utf-8',
        }
    },
    'handlers': {
        # 'file': {
        #     'level': 'DEBUG',
        #     'class': 'logging.FileHandler',
        #     'filename': BASE_DIR / 'django.log',
        #     'formatter': 'base_formatter',
        #     'encoding': 'utf-8',
        # },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'base_formatter',
        },
    },
    'loggers': {
        'Core': {
            'handlers': ['console'],  # ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # 'app_name': {
        #     'handlers':...
    },
}

if DEV:
    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True)
    INTERNAL_IPS = ('127.0.0.1',)
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
