"""File for custom errors handler in application."""


class FileExtensionError(Exception):
    """File extension error call if file extension is not valid."""


class TableIsNotFoundError(Exception):
    """This table is not in database."""
