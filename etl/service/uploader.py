"""Class for upload database data."""

import sqlite3
from typing import Iterator

from etl.core.database import BaseUploaderDatabase
from etl.core.errors import TableIsNotFoundError
from etl.models import model_mapper
from etl.models.base import IdMixing


class SQLiteUploader(BaseUploaderDatabase):
    """Class for upload data for SQLite database."""

    __slots__ = ('__dns', '__connection')

    def __init__(self, file_path: str, connection: sqlite3.Connection = None):
        """
        Initial function in SQLiteUploader.

        :param file_path: path to sqlite database file.
        :param connection: connection instance for database.
        """
        self.__connection = connection

        self.__dns = file_path

    def __create_connection(self) -> sqlite3.Connection:
        """Private function from create connection to database. Usage dns(path to sqlite file)."""
        if self.__dns is not None:
            self.__connection = sqlite3.connect(database=self.__dns)
            return self.__connection

        raise ValueError('Not connection param for connected to database.')

    def create_connection(self) -> sqlite3.Connection:
        """Create connection function."""
        if self.__connection is not None:
            return self.__connection

        return self.__create_connection()

    @property
    def get_connection(self) -> sqlite3.Connection:  # noqa: WPS615
        """Property for get private variable connection."""
        return self.__connection

    def _get_generator(self, model: type[IdMixing], query: str, iter_size: int) -> Iterator[list]:
        """Get generator date for upload data."""

    def extract_data(self, table: str, query: str, iter_size: int) -> Iterator[list]:
        """Extract data for sqlite database. Getting model and dataclass or raise Exception."""
        model = model_mapper.get(table, None)

        if not model:
            raise TableIsNotFoundError('This table in not found in database.')

        return self._get_generator(model, query, iter_size)
