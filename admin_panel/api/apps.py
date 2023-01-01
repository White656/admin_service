"""Config api application from admin panel."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Movies config from movies app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
