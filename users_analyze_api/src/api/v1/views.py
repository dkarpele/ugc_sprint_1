from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends

from models.views import View
from services.database import KafkaDep
from services.token import security_jwt, get_user_id

# Объект router, в котором регистрируем обработчики
router = APIRouter()


@router.post('/send-movie-time',
             response_model=View,
             status_code=HTTPStatus.CREATED,
             description="создание записи о просмотре",
             response_description="user_id, movie_id, begin_time, end_time")
async def create_view(token: Annotated[str, Depends(security_jwt)],
                      view: View, kafka: KafkaDep) -> View:
    user_id = await get_user_id(token)
    await kafka.produce_viewed_frame(user_id,
                               view.movie_id,
                               view.begin_time,
                               view.end_time)
    return view

