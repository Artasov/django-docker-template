import os
from pathlib import Path

env_get = os.environ.get

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env_get('SECRET_KEY')
DEBUG = bool(int(env_get('DEBUG')))
DEV = bool(int(env_get('DEV')))
SITE_ID = int(env_get('SITE_ID'))
ALLOWED_HOSTS = str(env_get('ALLOWED_HOSTS')).split(',')

AUTH_USER_MODEL = 'Core.User'

LOCAL_APPS = [
    'Core',
]
THIRD_APPS = [

]
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django.contrib.sites'
]

INSTALLED_APPS = LOCAL_APPS + THIRD_APPS + DJANGO_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

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

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
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
        'file': {
            'level': 'DEBUG' if DEBUG else 'WARNING',  # Уровень логирования. Выберите нужный уровень.
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'django.log',  # Имя файла, куда будут записываться логи.
            'formatter': 'base_formatter',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'Core': {
            'handlers': ['file'],
            'level': 'DEBUG' if DEBUG else 'WARNING',
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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
