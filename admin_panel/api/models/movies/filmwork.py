"""Film-work ORM model."""

from api.core.model.mixing import CreatedAndIdMixing
from config.components.constants import MAX_CHOICES_LENGTH
from django.db import models
from django.utils.translation import gettext_lazy as _


class FilmWorkTypeChoices(models.TextChoices):
    """Class choices from film work."""

    movie = 'MV', _('movies')
    tv_show = 'TV', _('tv_show')


class FilmWork(CreatedAndIdMixing):
    """Film-work model from django ORM."""

    title = models.TextField(_('Title film work'), null=False)
    description = models.TextField(_('Description film work'), blank=True)
    creation_date = models.DateTimeField(_('Creation film work date'), editable=False, auto_now_add=True)
    type = models.CharField(_('Film work type'), max_length=MAX_CHOICES_LENGTH, choices=FilmWorkTypeChoices.choices)
    rating = models.FloatField(_('Film work rating'))

    class Meta:  # noqa: D106, WPS306
        db_table = 'content\".\"film_work'
        verbose_name = _('Film work')
        verbose_name_plural = _('Film works')

    def __str__(self):
        return self.title
