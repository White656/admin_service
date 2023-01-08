"""Base class models for etl script."""

import datetime
import uuid
from dataclasses import dataclass, fields


@dataclass
class IdMixing(object):
    """Class from IdMixing in models for db ETL process."""

    id: uuid.UUID

    def __post_init__(self):
        # Loop through the fields
        for field in fields(self):
            # If there is a default and the value of the field is none we can assign a value
            if getattr(self, field.name) is None:
                setattr(self, field.name, str(datetime.datetime.now()))


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
