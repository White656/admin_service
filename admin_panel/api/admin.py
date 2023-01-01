"""Custom admin panels from admin panel service."""

from api.models.movies.filmwork import FilmWork, GenreFilmWork
from api.models.movies.genres import Genre
from api.models.movies.person import Person, PersonFilmWork
from django.contrib import admin


class GenreFilmWorkInline(admin.TabularInline):
    """Class from adaptive UI in admin panel."""

    model = GenreFilmWork


class PersonFilmWorkInline(admin.TabularInline):
    """Class from adaptive UI in admin panel."""

    model = PersonFilmWork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Class from Genre element in admin panel from this application."""


@admin.register(FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):
    """Class from FilmWork element in admin panel from this application."""

    inlines = (GenreFilmWorkInline, PersonFilmWorkInline)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Class from Person element in admin panel from this application."""


@admin.register(GenreFilmWork)
class GenreFilmWorkAdmin(admin.ModelAdmin):
    """Class from Genre film work element in admin panel from this application."""
