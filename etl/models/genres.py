"""File from base genre."""

import uuid
from dataclasses import dataclass

from etl.models.base import CreateAndUpdateMixing, CreateMixing, IdMixing


@dataclass
class Genres(IdMixing, CreateAndUpdateMixing):
    """Dataclass for genres table in database."""

    __slots__ = ('id', 'name', 'description', 'created_at', 'updated_at')

    name: str
    description: str


@dataclass
class GenreFilmWork(IdMixing, CreateMixing):
    """Dataclass for genres table in database."""

    __slots__ = ('id', 'genre', 'film_work', 'created_at')

    genre: uuid.UUID
    film_work: uuid.UUID
