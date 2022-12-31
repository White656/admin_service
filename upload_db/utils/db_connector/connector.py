"""Base file form ABC classes(database extractors)."""
from abc import ABC, abstractmethod


class Connector(ABC):
    """Base extractor from database. Describes base functional."""

    @abstractmethod
    def _create_connection(self, *args, **kwargs):
        """Create database connection if there is no previous, else cloe previous and create new."""
        raise NotImplementedError

    @property
    @abstractmethod
    def get_connection(self):
        """Get database connection from call method create_connection."""
        raise NotImplementedError

    @abstractmethod
    def close_connection(self, *args, **kwargs):
        """In finalize usage class close connection."""
        raise NotImplementedError
