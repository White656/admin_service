"""Constants in django admin panel service."""

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = 'static/'

MAX_LENGTH_IN_STRING = 256
MAX_CHOICES_LENGTH = 3
LIST_PER_PAGE = 25  # from admin panel
