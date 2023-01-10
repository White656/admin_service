"""Base class models for etl script."""

import datetime
import uuid
from dataclasses import dataclass


@dataclass
class IdMixing(object):
    """Class from IdMixing in models for db ETL process."""

    id: uuid.UUID


@dataclass
class CreateMixing(object):
    """Class from CreateMixing in models for db ETL process."""

    created_at: datetime.datetime


@dataclass
class UpdateMixing(object):
    """Class from UpdateMixing in models for db ETL process."""

    updated_at: datetime.datetime


@dataclass
class CreateAndUpdateMixing(CreateMixing, UpdateMixing):
    """Create and update Mixing for db ETL process."""
