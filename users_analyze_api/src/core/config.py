import os
from logging import config as logging_config
from pydantic import BaseSettings, Field

from core.logger import LOGGING

# Применяем настройки логирования
logging_config.dictConfig(LOGGING)


class MainConf(BaseSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class Settings(MainConf):
    project_name: str = Field(..., env='PROJECT_NAME')


settings = Settings()

