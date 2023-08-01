import os
from logging import config as logging_config
from pydantic import BaseSettings, Field
from dotenv import load_dotenv

from core.logger import LOGGING

# Применяем настройки логирования
logging_config.dictConfig(LOGGING)
load_dotenv()


class MainConf(BaseSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class Settings(MainConf):
    project_name: str = Field(..., env='PROJECT_NAME')
    host: str = Field(..., env='HOST_USERS_ANALYZE')
    port: int = Field(..., env='PORT_USERS_ANALYZE')


settings = Settings()


class KafkaCreds(MainConf):
    user: str = Field(..., env="KAFKA_USER")
    password: str = Field(..., env="KAFKA_PASSWORD")
    topic: str = Field(..., env='TOPIC')
    bootstrap_servers: list = os.environ.get('KAFKA_SERVERS').split()
    ssl_cafile: str = Field(..., env='KAFKA_CAFILE')


kafka_settings = KafkaCreds()