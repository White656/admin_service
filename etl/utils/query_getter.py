"""Tools for getting sql query to upload data into database."""
import json
from enum import Enum

from etl.core.config import settings


class TablesDatabase(str, Enum):
    """All table is script usage."""

    film_work = 'film_work'
    genre = 'genre'
    genre_film_work = 'genre_film_work'
    person = 'person'
    person_film_work = 'person_film_work'

    def __str__(self):
        """Magic method for get value from Enum."""
        return self.value


tables = TablesDatabase


def getter_query(table: TablesDatabase) -> str | None:
    """Function for get query from sql query json file."""
    with open(settings.query_file_name, 'r', encoding='utf-8') as query_file:
        return json.load(query_file).get(table)
