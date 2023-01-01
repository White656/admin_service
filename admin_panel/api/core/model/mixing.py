"""Base classes from django ORM."""
import uuid

from django.db import models


class IdMixing(models.Model):
    """Custom id mixing from django ORM."""

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False, blank=True)

    class Meta:  # noqa: D106, WPS306
        abstract = True


class CreatedMixing(models.Model):
    """Custom created/updated model from django ORM."""

    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:  # noqa: D106, WPS306
        abstract = True
        ordering = ['created_at']


class CreatedAndIdMixing(IdMixing, CreatedMixing):
    """Created and id mixing from django ORM."""

    class Meta:  # noqa: D106, WPS306
        abstract = True
        ordering = ['created_at']
