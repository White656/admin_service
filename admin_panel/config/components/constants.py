"""Constants in django admin panel service."""

import os

SECRET_KEY = os.getenv('SECRET_KEY')  # secret key from this application
DEBUG = os.environ.get('DEBUG', False) == 'True'  # debug mode in application

ROOT_URLCONF = 'config.urls'  # root url configuration path

WSGI_APPLICATION = 'config.wsgi.application'  # wsgi application path

LANGUAGE_CODE = 'ru-RU'  # language project

TIME_ZONE = 'UTC'  # time zone

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = 'static/'

MAX_LENGTH_IN_STRING = 256
MAX_CHOICES_LENGTH = 300
LIST_PER_PAGE = 25  # from admin panel
UPLOAD_FILM_WORK_FILE_PATH = 'movies/'  # from upload film work files
