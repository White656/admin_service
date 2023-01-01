"""Custom admin panels from admin panel service."""

from api.models.movies.genres import Genre
from django.contrib import admin


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Class from element in admin panel from this application."""
