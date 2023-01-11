"""File for upload data for postgres database."""

from base import DatabaseUploader
from psycopg2.extensions import connection as _connection


class PostgresUploader(DatabaseUploader):
    """Class for postgresSQL database uploader."""

    __slots__ = ('_connection',)

    def __init__(self, connection: _connection):
        """
        Initial file for setting variable in class.

        :param connection: connection postgres sql object.
        """
        self._connection: connection = connection

    def upload(self, query: str, **kwargs):
        """Function for upload data from postgres sql database."""
        __cur = self._connection.cursor()
        __cur.execute(query)
        return __cur.fetchall()
