"""Base class models for etl script."""
import datetime
import uuid
from dataclasses import dataclass
from typing import Any


@dataclass
class IdMixing(object):
    """Class from IdMixing in models for db ETL process."""

    __slots__ = ()

    id: uuid.UUID


@dataclass
class CreateMixing(object):
    """Class from CreateMixing in models for db ETL process."""

    __slots__ = ()
    created_at: Any | datetime.date


@dataclass
class UpdateMixing(object):
    """Class from UpdateMixing in models for db ETL process."""

    __slots__ = ()
    updated_at: Any | datetime.date


@dataclass
class CreateAndUpdateMixing(CreateMixing, UpdateMixing):
    """Create and update Mixing for db ETL process."""

    __slots__ = ()
