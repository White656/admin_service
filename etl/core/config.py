"""Configuration file from ETL script."""

import logging
from os import path

from dotenv import load_dotenv
from pydantic import BaseSettings, Field, PostgresDsn, validator

from etl.core.errors import FileExtensionError

load_dotenv()


class ApplicationConfig(BaseSettings):
    """Base application settings from ETL."""

    sqlite_path: str = Field('db.sqlite', description='Path to .sqlite database from upload data.')
    postgres_dns: PostgresDsn

    class Config:  # noqa:D106, WPS306
        env_prefix = 'etl_'
        env_file = '.env'
        env_file_encoding = 'utf-8'

    @validator('sqlite_path')
    def validate_data(cls, value: str):  # noqa: N805
        """
        Function for validation sqlite path variable in class.

        Raises:
            - FileNotFoundError: if file is not found or incorrect path to file.
            - FileExtensionError: If file extension is not valid.
        """
        is_path = path.exists(value)

        if not is_path:
            raise FileNotFoundError('This file is not found or incorrect path to file!')

        if not value.endswith('.sqlite'):
            raise FileExtensionError('This file extension is not valid!')

        return value


settings = ApplicationConfig()

logger = logging.getLogger(__name__)

logger_settings = {
    'format': '%(asctime)s - %(name)s.%(funcName)s:%(lineno)d - %(levelname)s - %(message)s',  # noqa: WPS323
    'datefmt': '%Y-%m-%d %H:%M:%S',  # noqa: WPS323
    'level': logging.INFO,
    'handlers': [logging.StreamHandler()],
}
