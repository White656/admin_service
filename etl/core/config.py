"""Configuration file from ETL script."""

from dotenv import load_dotenv
from pydantic import BaseSettings, Field, PostgresDsn

load_dotenv()


class ApplicationConfig(BaseSettings):
    """Base application settings from ETL."""

    sqlite_path: str = Field('db.sqlite', description='Path to .sqlite database from upload data.')
    postgres_dns: PostgresDsn

    class Config:  # noqa:D106,WPS306
        env_prefix = 'etl_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = ApplicationConfig()
