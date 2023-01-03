"""Custom admin panels from admin panel service."""

from api.core.admin.base import AdminPanelMixing
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
class GenreAdmin(AdminPanelMixing):
    """Class from Genre element in admin panel from this application."""

    list_display = ('name', 'created', 'modified')
    search_fields = ('name',)


@admin.register(FilmWork)
class FilmWorkAdmin(AdminPanelMixing):
    """Class from FilmWork element in admin panel from this application."""

    inlines = (GenreFilmWorkInline, PersonFilmWorkInline)
    list_display = ('title', 'type', 'rating', 'creation_date')


@admin.register(Person)
class PersonAdmin(AdminPanelMixing):
    """Class from Person element in admin panel from this application."""


@admin.register(GenreFilmWork)
class GenreFilmWorkAdmin(AdminPanelMixing):
    """Class from Genre film work element in admin panel from this application."""
