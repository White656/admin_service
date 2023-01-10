"""Dataclasses model from film_work model in database."""

import datetime
from dataclasses import dataclass, fields

from etl.models.base import CreateAndUpdateMixing, IdMixing

default_value_mapper = {
    'description': 'Testing description',
    'rating': 10.0,
    'creation_date': datetime.datetime.now(),
}


@dataclass(slots=True)
class FilmWork(IdMixing, CreateAndUpdateMixing):
    """Class from film work table in database."""

    title: str
    description: str
    creation_date: str | datetime.datetime
    type: str
    rating: float | int
    file_path: str

    def __post_init__(self):
        for field in fields(self):
            if getattr(self, field.name) is None and field.name in default_value_mapper:
                setattr(self, field.name, default_value_mapper[field.name])
