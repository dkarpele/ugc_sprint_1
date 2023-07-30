from models.model import Model
import uuid


class ClickHouseModel(Model):
    user_id: uuid.UUID
    movie_id: uuid.UUID
    viewed_frame: int
