"""File for upload data for sqlite database."""

import sqlite3

from etl.tests.service.base import DatabaseUploader


class SQLiteUploader(DatabaseUploader):
    """Class for upload data for database."""

    __slots__ = ('_connect',)

    def __init__(self, connection: sqlite3.Connection):
        """
        Initial function for class uploader.

        :param connection: sqlite3 object connection.
        """
        self._connect = connection

    def upload(self, query: str, **kwargs):
        """Function for upload database."""
        __cur = self._connect.cursor()
        __cur.execute(query)
        return __cur.fetchall()
