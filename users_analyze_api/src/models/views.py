from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class View(BaseModel):
    user_id: UUID
    movie_id: UUID
    begin_time: datetime
    end_time: datetime
