import logging
import uuid
from contextlib import asynccontextmanager

import uvicorn
from asgi_correlation_id import CorrelationIdMiddleware
from asgi_correlation_id.middleware import is_valid_uuid4
from fastapi import FastAPI, Depends, Request, status
from fastapi.responses import ORJSONResponse

from core.config import settings
from core.logger import LOGGING


async def startup():
    pass


async def shutdown():
    pass


@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup()
    yield
    await shutdown()


app = FastAPI(
    title=settings.project_name,
    description="Api to analyze users behaviour",
    version="1.0.0",
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    lifespan=lifespan)

# app.include_router(users.router, prefix='/api/v1/users', tags=['users'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=f'{settings.host}',
        port=settings.port,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
