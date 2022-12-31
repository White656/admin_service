"""This file describes the configuration of test scripts."""
import os

from pydantic import BaseSettings, Field, validator

"""
    - *dbname*: the database name
    - *database*: the database name (only as keyword argument)
    - *user*: user name used to authenticate
    - *password*: password used to authenticate
    - *host*: database host address (defaults to UNIX socket if not provided)
    - *port*: connection port number (defaults to 5432 if not provided)
"""


class DatabaseConfig(BaseSettings):
    """
    This class from configuration database connection (SQL database).
    """
    dbname: str = Field("movies_database", description="database table name.")
    user: str = Field("app", description="database user.")
    password: str = Field("123qwe", description="database password.")
    host: str = Field("localhost", description="database host usage.")
    port: int = Field(5432, description="database port.")
    options: str = Field("-c search_path=content", description="custom options in dsn.")

    @classmethod
    @validator("user")
    def custom_user_validator(cls, value):
        if value == "kirillhorkov":
            return "app"
        return value


class ApplicationConfig(BaseSettings):
    """
    From configuration application.
    """
    application_name: str = Field("White656", description="application name.")
    persons_count: int = Field(100000, description="persons count.")
    page_size: int = Field(5000, description="page size.")
    database: DatabaseConfig = DatabaseConfig()

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '__'


config = ApplicationConfig()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
