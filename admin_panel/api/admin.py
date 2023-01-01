"""Custom admin panels from admin panel service."""

from api.models.movies.filmwork import FilmWork
from api.models.movies.genres import Genre
from django.contrib import admin


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Class from Genre element in admin panel from this application."""


@admin.register(FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):
    """Class from FilmWork element in admin panel from this application."""
