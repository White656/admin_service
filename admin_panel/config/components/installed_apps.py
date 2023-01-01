"""Installed apps in admin panel application."""

BASED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MY_APPS = [
    'api.apps.ApiConfig',
]

INSTALLED_APPS = BASED_APPS + MY_APPS
