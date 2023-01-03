"""Class from base cache paginator."""

from config.components.cache import CACHE_TIMEOUT
from django.core.cache import cache
from django.core.paginator import Paginator
from django.utils.functional import cached_property

POSTFIX_CACHE_KEY = '_count'


class CachePaginator(Paginator):
    """Class from cache paginator."""

    @cached_property
    def count(self) -> int:
        """If not in cache storage return default value, else get value from cache."""
        cache_key = self.object_list.model.__name__ + POSTFIX_CACHE_KEY  # formatted cache key
        cache_value = cache.get(cache_key)  # get cache value

        if cache_value:
            return cache_value

        result = super().count  # get default function value
        cache.add(cache_key, result, CACHE_TIMEOUT)  # add result data in cache
        return result
