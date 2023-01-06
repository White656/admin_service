"""This file describes the configuration of test scripts."""

import os

from pydantic import BaseSettings, Field


class DatabaseConfig(BaseSettings):
    """This class from configuration database connection (SQL database)."""

    dbname: str = Field('movies_database', description='database table name.')
    user: str = Field('app', description='database user.')
    password: str = Field('123qwe', description='database password.')
    host: str = Field('localhost', description='database host usage.')
    port: int = Field(5432, description='database port.')  # noqa: WPS432
    options: str = Field('-c search_path=content', description='custom options for dsn.')


class ApplicationConfig(BaseSettings):
    """From configuration application."""

    application_name: str = Field('White656', description='application name.')
    persons_count: int = Field(100000, description='persons count.')  # noqa: WPS432
    page_size: int = Field(5000, description='page size.')  # noqa: WPS432
    database: DatabaseConfig = DatabaseConfig()

    class Config:  # noqa: WPS306
        """Class configuration application config."""

        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '__'


config = ApplicationConfig()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
