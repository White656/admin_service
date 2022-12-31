"""This file from pg extractor class. Used in database connection and load/upload data."""
import psycopg2
from psycopg2._psycopg import cursor
from psycopg2.extensions import connection as conn
from psycopg2.extras import DictCursor

from example_usage.core.config import DatabaseConfig
from example_usage.utils.db_connector.connector import Connector


class PostgresConnector(Connector):
    """
    PostgresSQL database extractor.
    """
    __instance = None

    __slots__ = ('__config', '__postgres_connection')

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self) -> None:
        self.__class__.__instance = None

    def __init__(self, dns: DatabaseConfig,
                 postgres_connection: conn | None = None) -> None:
        self.__config = dns
        self.__postgres_connection = postgres_connection

    def _create_connection(self) -> conn:
        """
        This function create new connection from PostgresSQL database.
        :return: Connection psql object.
        """
        if self.__postgres_connection is not None:
            self.__postgres_connection.close()

        self.__postgres_connection = psycopg2.connect(**self.__config.dict(), cursor_factory=DictCursor)

        return self.__postgres_connection

    @property
    def get_connection(self) -> conn:
        """
        This function get connection fron PostgresSQL database.
        :return: connection psql object.
        """
        if self.__postgres_connection is None or self.__postgres_connection.closed:
            self.__postgres_connection = self._create_connection()

        return self.__postgres_connection

    def close_connection(self) -> bool:
        """
        This function close PostgresSQL connection.
        :return: If connection is success closed return True, else return False.
        """
        return self.__postgres_connection.close()

    @property
    def get_cursor(self) -> cursor:
        return self.get_connection.cursor()

    def __str__(self) -> str:
        return f"is_connection: {True if self.__postgres_connection else False}"

    def __repr__(self):
        return f"connection: {self.__postgres_connection}, dns: {self.__config}"
