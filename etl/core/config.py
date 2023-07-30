from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    redis_host: str = Field(..., env='REDIS_HOST')
    redis_port: int = Field(..., env='REDIS_PORT')
    kafka_bootstrap_server: list = Field(..., env='KAFKA_BOOTSTRAP_SERVERS')
    topic: str = Field(..., env='TOPIC')
    group_id_clickhouse: str = Field(..., env='GROUP_ID_CLICKHOUSE')
    batch_size_clickhouse: int = Field(..., env='BATCH_SIZE_CLICKHOUSE')
    timeout_clickhouse: int = Field(..., env='TIMEOUT_CLICKHOUSE')
    clickhouse_server: str = Field(..., env='CLICKHOUSE_SERVER')

    class Config:
        env_file = '.env'


settings = Settings()
