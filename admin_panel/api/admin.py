"""Custom admin panels from admin panel service."""

from api.core.admin.base import AdminPanelMixing
from api.models.movies.filmwork import FilmWork, GenreFilmWork
from api.models.movies.genres import Genre
from api.models.movies.person import Person, PersonFilmWork
from django.contrib import admin


class GenreFilmWorkInline(admin.TabularInline):
    """Class from adaptive UI in admin panel."""

    model = GenreFilmWork
    list_prefetch_related = ('genre', 'film_work')
    autocomplete_fields = ('genre', 'film_work')


class PersonFilmWorkInline(admin.TabularInline):
    """Class from adaptive UI in admin panel."""

    model = PersonFilmWork
    list_prefetch_related = ('person', 'film_work')
    autocomplete_fields = ('person', 'film_work')


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

    list_prefetch_related = ('genres', 'persons')
    autocomplete_fields = ('genres', 'persons')

    search_fields = ('title', 'description', 'id')

    def get_queryset(self, request):
        """Function from custom get query set from django admin panel."""
        return super().get_queryset(request).prefetch_related(*self.list_prefetch_related)


@admin.register(Person)
class PersonAdmin(AdminPanelMixing):
    """Class from Person element in admin panel from this application."""

    list_display = ('full_name',)
    search_fields = ('full_name',)
