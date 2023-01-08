"""Dataclasses model from film_work model in database."""

import datetime
from dataclasses import dataclass

from etl.models.base import CreateAndUpdateMixing, IdMixing


@dataclass(slots=True)
class FilmWork(IdMixing, CreateAndUpdateMixing):
    """Class from film work table in database."""

    title: str
    description: str
    creation_date: str | datetime.datetime
    type: str
    rating: float | int
    file_path: str
