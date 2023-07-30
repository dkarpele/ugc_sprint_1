from clickhouse_driver import Client
from kafka import KafkaConsumer

from core.config import settings
from services.clickhouse import ClickHouseLoader


def etl_clickhouse() -> None:
    """ETL from Kafka to ClickHouse"""
    clickhouse_loader = ClickHouseLoader(
        consumer=KafkaConsumer(
            settings.topic,
            enable_auto_commit=False,
            bootstrap_servers=settings.kafka_bootstrap_server,
            group_id=settings.group_id_clickhouse,
            consumer_timeout_ms=settings.timeout_clickhouse * 1000
        ),
        clickhouse=Client(settings.clickhouse_server)
    )

    while True:
        clickhouse_loader.get_kafka_data(
            batch_size=settings.batch_size_clickhouse
        )


if __name__ == '__main__':
    etl_clickhouse()
