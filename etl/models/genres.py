"""File from base genre."""

import uuid
from dataclasses import dataclass

from etl.models.base import CreateAndUpdateMixing, CreateMixing, IdMixing


@dataclass(slots=True)
class Genres(IdMixing, CreateAndUpdateMixing):
    """Dataclass for genres table in database."""

    name: str
    description: str


@dataclass(slots=True)
class GenreFilmWork(IdMixing, CreateMixing):
    """Dataclass for genres table in database."""

    genre_id: uuid.UUID
    film_work_id: uuid.UUID
