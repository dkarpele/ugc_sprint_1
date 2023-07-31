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
    kafka.create_post(view.user_id, view.movie_id, view.begin_time, view.end_time)
    return view
