from datetime import datetime
from uuid import UUID

from models.model import Model


class View(Model):
    user_id: UUID
    movie_id: UUID
    begin_time: datetime
    end_time: datetime
