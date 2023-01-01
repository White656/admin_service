"""Database settings in admin panel application."""

import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('POSTGRES_DB_PORT', 5432),  # noqa: WPS432
        'OPTIONS': {
            # Нужно явно указать схемы, с которыми будет работать приложение.
            'options': '-c search_path=public,content',
        },
    },
}
