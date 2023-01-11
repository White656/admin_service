"""Main file for run test etl script."""
import sqlite3

from psycopg2 import connect
from psycopg2.extensions import connection as _connection

from etl.core.manager import conn_context
from etl.tests.check_consistency.config import settings


def test_database(sqlite_connection: sqlite3.Connection, postgres_connection: _connection):
    """Main function for check etl script."""

    ...


postgres_dns = settings.postgres_dns
sqlite_dns = settings.sqlite_path

if __name__ == '__main__':
    with connect(postgres_dns, ) as conn, conn.cursor() as cursor, conn_context(settings.sqlite_path) as sqlite_conn:
        ...
