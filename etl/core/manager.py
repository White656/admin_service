"""File from simple context manager."""

import sqlite3
from contextlib import contextmanager


def dict_factory(curs: sqlite3.Cursor, row: tuple) -> dict:
    """Factory for view SQLite cursor as dict."""
    result = {}
    for idx, col in enumerate(curs.description):
        result[col[0]] = row[idx]
    return result


@contextmanager
def conn_context(db_path: str):
    """
    Function for create context manager for database connection.

    Args:
        db_path: path to database.

    Yields:
        database connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = dict_factory
    yield conn
    conn.close()
