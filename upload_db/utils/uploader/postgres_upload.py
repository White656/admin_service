"""This file from descriptions of data loading class in postgresQL."""
from psycopg2.extras import execute_batch

from upload_db.utils.db_connector.pg_connector import PostgresConnector
from upload_db.utils.uploader.upload import BaseDatabaseUpload


class PostgresUploader(BaseDatabaseUpload, PostgresConnector):
    """PostgresSQL uploader."""

    def upload(self, query: str, params: list | tuple | set, page_size: int = None) -> None:
        """
        This function from upload data in PostgresSQL.

        :param page_size: size page to insert into table.
        :param query: all data from upload.
        :param params: Typed list. Example [(id, name, created, modified)].
        :return: Nothing.
        """
        execute_batch(self.get_cursor, query, params, page_size=page_size)
        self.get_connection.commit()
