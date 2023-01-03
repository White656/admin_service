"""Base classes from admin panel."""

from api.core.pagination.cache_paginator import CachePaginator
from config.components.constants import LIST_PER_PAGE
from django.contrib import admin


class AdminPanelMixing(admin.ModelAdmin):
    """This class from custom admin panel params."""

    list_per_page = LIST_PER_PAGE

    paginator = CachePaginator

    show_full_result_count = False
