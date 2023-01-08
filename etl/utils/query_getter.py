"""Tools for getting sql query to upload data into database."""

from enum import Enum


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

get_count = """SELECT COUNT(*) FROM {table}"""  # noqa: WPS322
get_limited = """SELECT * FROM {table} LIMIT {start}, {end}"""  # noqa: WPS322
insert = """INSERT INTO {table} {column} VALUES {values} ON CONFLICT (id) DO NOTHING;"""  # noqa: WPS322
