"""This file contains functions that will help in the formation of queries."""
from enum import Enum


class QueryVariants(str, Enum):
    """This class from query variants."""

    into_person = "insert_into_person.txt"
    into_person_film_work = "insert_into_person_film_work.txt"
    get_all_film_work = "get_all_film_work.txt"

    def __str__(self):
        return self.value


variants = QueryVariants


def get_query_from_file(variant: variants) -> str | None:
    """
    This function from read sql query from file.

    :param variant: filename from current dir.
    :return: file date(some sql query).
    """
    with open(f"query/{variant}", "r", encoding="utf-8") as file:
        return file.read().replace('\n', ' ')
