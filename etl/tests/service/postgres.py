"""File for upload data for postgres database."""

from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor
from service.base import DatabaseUploader


class PostgresUploader(DatabaseUploader):
    """Class for postgresSQL database uploader."""

    __slots__ = ('_connection',)

    def __init__(self, connection: _connection):
        """
        Initial file for setting variable in class.

        :param connection: connection postgres sql object.
        """
        self._connection: connection = connection

    @property
    def get_cursor(self):
        """Method for get database cursor (usage custom cursor factory)."""
        return self._connection.cursor(cursor_factory=DictCursor)

    def upload(self, query: str, is_one: bool = False, **kwargs):
        """Function for upload data from postgres sql database."""
        __cur = self.get_cursor
        __cur.execute(query)
        if is_one:
            return __cur.fetchone()
        return __cur.fetchall()
