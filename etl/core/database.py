"""File for bases classes for database."""
from abc import ABC, abstractmethod


class BaseUploaderDatabase(ABC):
    """Class for base uploader API database."""

    @abstractmethod
    def _get_generator(self, *args, **kwargs):
        """Function getter generator for data."""
        raise NotImplementedError

    @abstractmethod
    def extract_data(self, *args, **kwargs):
        """Extract data function."""  # TODO write commentaries to function
        raise NotImplementedError


class BaseLoaderDatabase(ABC):
    """Class for base API Loader database."""

    @abstractmethod
    def upload(self, *args, **kwargs):
        """Base upload to database function."""
        raise NotImplementedError
