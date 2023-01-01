"""Genres ORM model."""

from api.core.model.mixing import CreatedAndIdMixing
from config.components.constants import MAX_LENGTH_IN_STRING
from django.db import models
from django.utils.translation import gettext_lazy as _


class Genre(CreatedAndIdMixing):
    """Genres model from django ORM."""

    name = models.CharField(_('Genres name'), max_length=MAX_LENGTH_IN_STRING, null=False)
    description = models.TextField(_('Description genre'), blank=True)

    class Meta:  # noqa: D106, WPS306
        db_table = 'content\".\"genre'
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')

    def __str__(self):
        return self.name
