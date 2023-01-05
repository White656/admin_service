"""File from simple context manager."""

import sqlite3
from contextlib import contextmanager


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
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()
