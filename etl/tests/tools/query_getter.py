"""File for getting query for upload data fom database."""

from enum import Enum


class QueryEnum(str, Enum):
    """Enum class for getting table name into database."""

    film_work = 'film_work'
    genre = 'genre'
    genre_film_work = 'genre_film_work'
    person = 'person'
    person_film_work = 'person_film_work'

    def __str__(self):
        return self.value


tables = QueryEnum

get_all_data = 'SELECT * FROM {table}'
count_all_data = 'SELECT COUNT(*) FROM {table}'


def get_query_for_all_data_and_count(table: tables) -> tuple[str, str]:
    """
    Function for get query for get all values from database and count values into database.

    :param table: table name.
    :return: Return two value. First - query for get all values in database, third - query for get all count values.
    """
    return get_all_data.format(table=table), count_all_data.format(table=table)
