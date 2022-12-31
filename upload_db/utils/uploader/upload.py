"""This file from ABC classes from upload data."""
from abc import ABC, abstractmethod


class BaseDatabaseUpload(ABC):
    """This class ABC uploader data in database."""

    @abstractmethod
    def upload(self, *args, **kwargs):
        """
        This function from upload data in database.

        :return: If data upload is success return True, else, False.
        """
        raise NotImplementedError
