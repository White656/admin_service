"""Main file for run test etl script."""
import sqlite3

from psycopg2 import connect
from psycopg2.extensions import connection as _connection
from service.postgres import PostgresUploader
from service.sqlite import SQLiteUploader
from tools.query_getter import get_query_for_all_data_and_count, tables

from etl.core.manager import conn_context
from etl.tests.check_consistency.config import settings


def check_valid_len_tables(count_in_pg: list[int], count_in_sql: dict):
    assert count_in_pg[0] == count_in_sql.get('COUNT(*)'), ValueError('The length of the tables is not comparable!')


def test_database(sqlite_connection: sqlite3.Connection, postgres_connection: _connection, table: str | tables):
    """Main function for check etl script."""
    pg_upload = PostgresUploader(postgres_connection)
    sql_upload = SQLiteUploader(sqlite_connection)
    all_data_query, count_query = get_query_for_all_data_and_count(table)

    check_valid_len_tables(pg_upload.upload(count_query, is_one=True), sql_upload.upload(count_query))


postgres_dns = settings.postgres_dns
sqlite_dns = settings.sqlite_path

if __name__ == '__main__':
    with connect(postgres_dns, ) as conn, conn_context(settings.sqlite_path) as sqlite_conn:

        for table in tables:
            test_database(sqlite_conn, conn, table)
            break
