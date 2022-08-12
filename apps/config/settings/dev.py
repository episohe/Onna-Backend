"""
Django dev settings for KETI project.
settings/dev.py
"""
from ._base import *

DEBUG = env.DEV_DEBUG

ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'config.wsgi.dev.application'

INSTALLED_APPS += [
    'debug_toolbar',
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env.DEV_DB_HOST,
        "USER": env.DEV_DB_USERNAME,
        "PASSWORD": env.DEV_DB_PASSWORD.get_secret_value(),
        "NAME": env.DEV_DB_NAME,
    }
}
