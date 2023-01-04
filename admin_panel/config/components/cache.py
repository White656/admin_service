"""File from cache configuration."""
import os

from config.components.constants import DEBUG

CACHE_TIMEOUT = 36000

CACHE_CONFIG = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': f'redis://{os.environ.get("REDIS_HOST")}:{os.environ.get("REDIS_PORT")}',  # noqa: WPS237, WPS305
        'OPTIONS': {
            'parser_class': 'redis.connection.PythonParser',
            'pool_class': 'redis.BlockingConnectionPool',
        },
    },
}

if DEBUG:
    CACHE_CONFIG = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        },
    }

CACHES = {
    **CACHE_CONFIG,
}
