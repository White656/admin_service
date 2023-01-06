"""Person film work dataclass from ETL script."""

import uuid
from dataclasses import dataclass

from etl.models.base import CreateAndUpdateMixing, CreateMixing, IdMixing


@dataclass
class Person(IdMixing, CreateAndUpdateMixing):
    """Dataclass for person table in database."""

    __slots__ = ('id', 'full_name', 'created_at', 'updated_at')

    full_name: str


@dataclass
class PersonFilmWork(IdMixing, CreateMixing):
    """Dataclass for person film work table in database."""

    __slots__ = ('id', 'film_work', 'person', 'role', 'created_at')

    film_work: uuid.UUID
    person: uuid.UUID
    role: str
