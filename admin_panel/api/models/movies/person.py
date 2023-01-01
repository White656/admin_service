"""Person ORM model."""

from api.core.model.mixing import CreatedAndIdMixing, IdMixing
from config.components.constants import (MAX_CHOICES_LENGTH,
                                         MAX_LENGTH_IN_STRING)
from django.db import models
from django.utils.translation import gettext_lazy as _


class PersonTypeChoices(models.TextChoices):
    """Class choices from film work."""

    director = 'DR', _('director')
    producer = 'PR', _('producer')
    participant = 'pt', _('participant')


class Person(CreatedAndIdMixing):
    """Person model from django ORM."""

    full_name = models.CharField(_('Person full name'), max_length=MAX_LENGTH_IN_STRING, blank=False)

    class Meta:  # noqa: D106, WPS306
        db_table = 'content\".\"person'
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')

    def __str__(self):
        return self.full_name


class PersonFilmWork(IdMixing):
    """Person film work M2M from django ORM."""

    film_work = models.ForeignKey('FilmWork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    role = models.CharField(_('Person role'), choices=PersonTypeChoices.choices, max_length=MAX_CHOICES_LENGTH)
    created = models.DateTimeField(_('Created person film work connection'), auto_now_add=True, editable=False)

    class Meta:  # noqa: D106, WPS306
        db_table = 'content\".\"person_film_work'
