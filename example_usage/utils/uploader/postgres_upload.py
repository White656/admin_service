"""This file from descriptions of data loading class in postgresQL."""
from example_usage.utils.db_connector.pg_connector import PostgresConnector
from example_usage.utils.uploader.upload import BaseDatabaseUpload

from psycopg2.extras import execute_batch


class PostgresUploader(BaseDatabaseUpload, PostgresConnector):
    """
    PostgresSQL uploader.
    """

    def upload(self, query: str, params: list | tuple | set, page_size: int = None) -> None:
        """
        This function from upload data in PostgresSQL.
        :param query: all data from upload.
        :param params: Typed list. Example [(id, name, created, modified)].
        :return: Nothing.
        """
        _cur = self.get_cursor
        execute_batch(_cur, query, params, page_size=page_size)
        _cur.close()
