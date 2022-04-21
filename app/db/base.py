from ormar import ModelMeta

from app.db.config import database
from app.db.meta import meta


class BaseMeta(ModelMeta):
    """Base metadata for models."""

    database = database
    metadata = meta
