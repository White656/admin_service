"""File from cache configuration."""
import os

CACHE_TIMEOUT = 3600
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': f'redis://{os.environ.get("REDIS_HOST")}:{os.environ.get("REDIS_PORT")}',  # noqa: WPS237, WPS305
    },
}
