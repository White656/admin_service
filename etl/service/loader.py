"""Service to load data in database."""
from typing import Iterator

import psycopg2
from psycopg2.extensions import connection
from pydantic import PostgresDsn

from etl.core.database import BaseLoaderDatabase
from etl.models.base import IdMixing


class PostgresSaver(BaseLoaderDatabase):
    """Class to load data in postgres sql database."""

    __slots__ = ('_connection', '_dns')

    def __init__(self, conn: connection, dns: PostgresDsn = None) -> None:
        """
        Initial function to PostgresLoader class.

        :param conn: PostgresSQL connection object.
        :param dns: configuration to set connection.
        """
        self._connection = conn
        self._dns = dns

    def _create_connection(self) -> connection:
        """
        Function for create new connection for database. Closed all old connection before create new.

        :return: Postgres connection object.
        """
        if self._connection is not None:
            self._connection.close()

        return psycopg2.connect(dns=self._dns)

    @property
    def get_connection(self) -> connection:  # noqa:WPS615
        """
        Property for get connection to postgres.

        :return: database connection object.
        """
        if self._connection is None or self._connection.closed:
            return self._create_connection()
        return self._connection

    @classmethod
    def _generate_query(
            cls, query: str, data: Iterator[type[IdMixing]], model: type[IdMixing], table: str,
    ) -> str | bool:
        """Function from generated query to insert into database."""
        *res, = data  # noqa: WPS460, WPS356 TODO fix list view and update for load in database.

        if not data:
            return False

        return query.format(table=table, column=str(model.__slots__).replace("'", '"'), values=res)

    def upload(self, query: str, data: Iterator[type[IdMixing]], model: type[IdMixing], table: str) -> None:
        """Function for bulk upload data in database."""
        query = self._generate_query(query, data, model, table)  # TODO fix query

        if not query:
            return

        cursor = self._connection.cursor()
        cursor.execute(query)
        self._connection.commit()
