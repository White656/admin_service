"""Mail file into etl script."""

import sqlite3
from typing import Iterator

from psycopg2 import connect
from psycopg2.extensions import connection as _connection

from etl.core.config import settings
from etl.core.manager import conn_context
from etl.service.loader import PostgresSaver
from etl.service.uploader import SQLiteUploader
from etl.utils.query_getter import get_count, get_limited, insert, tables


def get_query(start: int, end: int, period: int) -> Iterator:
    if end % period != 0:
        return range(start, (end + (period - (end % period))) + 1, period)
    return range(start, end, period)


def load_from_sqlite(connection: sqlite3.Connection, pg_conn: _connection, table: str,
                     query_to_upload: str, query_to_insert: str):
    """Основной метод загрузки данных из SQLite в Postgres"""

    postgres_saver = PostgresSaver(pg_conn)
    sqlite_uploader = SQLiteUploader(connection)

    data, model = sqlite_uploader.extract_data(table=table, query=query_to_upload)

    postgres_saver.upload(query_to_insert, data, model, table)


postgres_dns = settings.postgres_dns
if __name__ == '__main__':

    with connect(postgres_dns, ) as conn, conn.cursor() as cursor, conn_context(settings.sqlite_path) as sqlite_conn:
        for table in tables:
            sqlite_cursor = sqlite_conn.cursor()
            sqlite_cursor.execute(get_count.format(table=table))
            count = sqlite_cursor.fetchall()[0].get("COUNT(*)")
            for count, item in enumerate(get_query(0, count, settings.number_to_upload)):
                getting_query = get_limited.format(table=table,
                                                   start=count * settings.number_to_upload - settings.number_to_upload,
                                                   end=item)

                load_from_sqlite(sqlite_conn, conn, table, getting_query, insert)

            sqlite_cursor.close()
