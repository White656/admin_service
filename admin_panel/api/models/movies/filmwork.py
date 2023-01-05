"""Film-work ORM models."""

from api.core.model.mixing import CreatedAndIdMixing, IdMixing
from config.components.constants import (MAX_CHOICES_LENGTH,
                                         MAX_LENGTH_IN_STRING,
                                         UPLOAD_FILM_WORK_FILE_PATH)
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class FilmWorkTypeChoices(models.TextChoices):
    """Class choices from film work."""

    movie = 'MV', _('movies')
    tv_show = 'TV', _('tv_show')


class FilmWork(CreatedAndIdMixing):
    """Film-work models from django ORM."""

    title = models.TextField(_('Title film work'), null=False)
    description = models.TextField(_('Description film work'), blank=True)
    creation_date = models.DateTimeField(_('Creation film work date'), editable=False, auto_now_add=True)
    type = models.CharField(_('Film work type'), max_length=MAX_CHOICES_LENGTH, choices=FilmWorkTypeChoices.choices)
    rating = models.FloatField(_('Film work rating'), validators=[MinValueValidator(0), MaxValueValidator(100)])
    file_path = models.FileField(
        _('file path'), max_length=MAX_LENGTH_IN_STRING, blank=True, null=True, upload_to=UPLOAD_FILM_WORK_FILE_PATH,
    )
    genres = models.ManyToManyField('Genre', through='GenreFilmWork')
    persons = models.ManyToManyField('Person', through='PersonFilmWork')

    class Meta:  # noqa: D106, WPS306
        db_table = 'content\".\"film_work'
        verbose_name = _('Film work')
        verbose_name_plural = _('Film works')

    def __str__(self):
        return self.title


class GenreFilmWork(IdMixing):
    """Genre film work M2M from django ORM."""

    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    film_work = models.ForeignKey('FilmWork', on_delete=models.CASCADE)
    created_at = models.DateTimeField(_('Created genre film work'), auto_now_add=True)

    class Meta:  # noqa: D106, WPS306
        db_table = 'content\".\"genre_film_work'
