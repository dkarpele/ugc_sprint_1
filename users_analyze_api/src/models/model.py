import orjson

from fastapi import Query
from pydantic import BaseModel

import src.core.config as conf


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class Model(BaseModel):
    class Config:
        # Заменяем стандартную работу с json на более быструю
        json_loads = orjson.loads
        json_dumps = orjson_dumps
        allow_population_by_field_name = True
