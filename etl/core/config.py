"""Configuration file from ETL script."""

import logging

from dotenv import load_dotenv
from pydantic import BaseSettings, Field, PostgresDsn, validator

from etl.core.errors import FileExtensionError

load_dotenv()

DEFAULT_UPLOAD_NUMBER = 100


class ApplicationConfig(BaseSettings):
    """Base application settings from ETL."""

    sqlite_path: str = Field('db.sqlite', description='Path to .sqlite database from upload data.')
    postgres_dns: PostgresDsn
    query_file_name: str = Field('utils/query.json', description='Path to .json file for get sql query.')
    number_to_upload: int = Field(DEFAULT_UPLOAD_NUMBER, description='Upload data for database.')

    class Config:  # noqa:D106, WPS306
        env_prefix = 'etl_'
        env_file = '.env'
        env_file_encoding = 'utf-8'

    @validator('sqlite_path')
    def validate_data(cls, value: str):  # noqa: N805
        """
        Function for validation sqlite path variable in class.

        Raises:
            - FileExtensionError: If file extension is not valid.
        """
        if not value.endswith('.sqlite'):
            raise FileExtensionError('This file extension is not valid!')

        return value

    @validator('query_file_name')
    def validate_query(cls, value: str):  # noqa: N805
        """
        Function fof validation json path variable in class.

        Raises:
             - FileExtensionError: if file extension is not valid.
        """
        if not value.endswith('.json'):
            raise FileExtensionError('This file extension is not valid! Recommend usage .json file.')

        return value


settings = ApplicationConfig()

logger = logging.getLogger(__name__)

logger_settings = {
    'format': '%(asctime)s - %(name)s.%(funcName)s:%(lineno)d - %(levelname)s - %(message)s',  # noqa: WPS323
    'datefmt': '%Y-%m-%d %H:%M:%S',  # noqa: WPS323
    'level': logging.INFO,
    'handlers': [logging.StreamHandler()],
}
