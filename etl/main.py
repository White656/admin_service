"""Mail file into etl script."""

import sqlite3

from psycopg2.extensions import connection as _connection

from etl.core.config import settings


class PostgresSaver:
    ...


class SQLiteLoader:
    ...


def load_from_sqlite(connection: sqlite3.Connection, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""

    postgres_saver = PostgresSaver(pg_conn)
    sqlite_loader = SQLiteLoader(connection)

    data = sqlite_loader.load_movies()
    postgres_saver.save_all_data(data)


postgres_dns = settings.postgres_dns
# with psycopg2.connect(postgres_dns, ) as conn, conn.cursor() as cursor:
#     for element in mapper:
#         cursor.execute(f"""SELECT * FROM content.{element};""")
#         data = cursor.fetchall()
#         print(data)
