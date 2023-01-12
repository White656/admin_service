"""Configuration file for test etl script."""

from dotenv import load_dotenv
from pydantic import BaseSettings, Field, PostgresDsn, validator

from etl.core.errors import FileExtensionError

load_dotenv()


class ApplicationSetting(BaseSettings):
    """Class for application setting for etl script."""

    postgres_dns: PostgresDsn
    sqlite_path: str = Field('../db.sqlite', description='path to db.sqlite file')

    class Config:  # noqa: D106, WPS306
        env_prefix = 'tests_'
        env_file = '.env'
        env_file_encoding = 'utf-8'

    @validator('sqlite_path')
    def validate_date(cls, value: str):  # noqa: N805
        """
        Function for validation sqlite path variable in class.

        Raises:
            - FileExtensionError: If file extension is not valid.
        """
        if not value.endswith('.sqlite'):
            raise FileExtensionError('This file extension is not valid!')

        return value


settings = ApplicationSetting()
