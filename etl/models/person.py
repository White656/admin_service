"""Person film work dataclass from ETL script."""

import uuid
from dataclasses import dataclass

from etl.models.base import CreateAndUpdateMixing, CreateMixing, IdMixing


@dataclass(slots=True)
class Person(IdMixing, CreateAndUpdateMixing):
    """Dataclass for person table in database."""

    full_name: str


@dataclass(slots=True)
class PersonFilmWork(IdMixing, CreateMixing):
    """Dataclass for person film work table in database."""

    film_work_id: uuid.UUID
    person_id: uuid.UUID
    role: str
