"""Base classes for testing etl script."""

from abc import ABC, abstractmethod


class DatabaseUploader(ABC):
    """Abstract class for db uploader."""

    @abstractmethod
    def upload(self, **kwargs):
        """Real signature is unknown."""
        raise NotImplementedError
