"""
Django dev settings for KETI project.
settings/dev.py

prod 실행은
python manage.py runserver --settings=config.settings.prod
"""

DEBUG = False

# ALLOWED_HOSTS = ['*']
#
# WSGI_APPLICATION = 'config.wsgi.dev.application'
#
# INSTALLED_APPS += []
#
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "HOST": env.DB_HOST,
#         "USER": env.DB_USERNAME,
#         "PASSWORD": env.DB_PASSWORD.get_secret_value(),
#         "NAME": env.DB_NAME,
#     }
# }
