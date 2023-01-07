"""Service to load data in database."""
from typing import Iterator

import psycopg2
from pydantic import PostgresDsn

from etl.core.database import BaseLoaderDatabase
from etl.models.base import IdMixing


class PostgresLoader(BaseLoaderDatabase):
    """Class to load data in postgres sql database."""

    __slots__ = ('_connection', '_dns')

    def __init__(self, conn: psycopg2.connection, dns: PostgresDsn) -> None:
        """
        Initial function to PostgresLoader class.

        :param conn: PostgresSQL connection object.
        :param dns: configuration to set connection.
        """
        self._connection = conn
        self._dns = dns

    def _create_connection(self) -> psycopg2.connection:
        """
        Function for create new connection for database. Closed all old connection before create new.

        :return: Postgres connection object.
        """
        if self._connection is not None:
            self._connection.close()

        return psycopg2.connect(dns=self._dns)

    @property
    def get_connection(self) -> psycopg2.connection:  # noqa:WPS615
        """
        Property for get connection to postgres.

        :return: database connection object.
        """
        if self._connection is None or self._connection.closed:
            return self._create_connection()
        return self._connection

    def upload(self, *args, **kwargs):
        """Function for bulk upload data in database."""

    def _generate_query(self, query: str, data: Iterator[type[IdMixing]]):
        """Generated query for upload data in database."""
