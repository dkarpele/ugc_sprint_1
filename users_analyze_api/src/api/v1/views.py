from http import HTTPStatus

from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, HTTPException

from models.views import View
from services.database import KafkaDep

# Объект router, в котором регистрируем обработчики
router = APIRouter()


@router.post('/send-movie-time',
             response_model=View,
             status_code=HTTPStatus.CREATED,
             description="создание записи о просмотре",
             response_description="user_id, movie_id, begin_time, end_time")
async def create_view(view: View, kafka: KafkaDep) -> View:
    kafka.producer.send(
        topic=kafka.topic,
        value=' '.join([str(view.begin_time), str(view.end_time)]).encode('utf-8'),
        key=' '.join([str(view.user_id), str(view.movie_id)]).encode('utf-8')
    )
    return view
