from clickhouse_driver import Client
from kafka import KafkaConsumer

from models.views import ClickHouseModel
from services.backoff import backoff


class ClickHouseLoader:
    SQL_CREATE_RECORD = """
    INSERT INTO user_viewed_frame (user_id, movie_id, viewed_frame) VALUES {data};
    """

    def __init__(
            self,
            consumer: KafkaConsumer,
            clickhouse: Client
    ) -> None:
        self.consumer = consumer
        self.clickhouse = clickhouse

    @backoff(service='ClickHouse')
    def get_kafka_data(self, batch_size: int = 1000) -> None:
        cache = []
        for message in self.consumer:
            user_id, movie_id = message.key.decode().split("+")
            cache.append(ClickHouseModel(
                user_id=user_id,
                movie_id=movie_id,
                viewed_frame=message.value.decode()
            ))
            if len(cache) >= batch_size:
                self._set_data_in_clickhouse(cache)
        if cache:
            self._set_data_in_clickhouse(cache)

    @backoff(service='ClickHouse')
    def _set_data_in_clickhouse(self, cache):
        query = self.SQL_CREATE_RECORD.format(
            data=", ".join([f"('{i.user_id}', "
                            f"'{i.movie_id}', "
                            f"{i.viewed_frame})" for i in cache])
        )
        self.clickhouse.execute(query)