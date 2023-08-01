from kafka import KafkaProducer, KafkaConsumer

from core.config import kafka_settings


class Kafka:
    def __init__(self, topic: str):
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=kafka_settings.bootstrap_servers,
            security_protocol="SASL_SSL",
            sasl_mechanism="SCRAM-SHA-512",
            sasl_plain_username=kafka_settings.user,
            sasl_plain_password=kafka_settings.password,
            ssl_cafile=kafka_settings.ssl_cafile
        )

    def produce_viewed_frame(self, user_id: str, movie_id: str, begin_time, end_time):
        self.producer.send(
            topic=self.topic,
            key='%'.join([str(user_id), str(movie_id)]).encode('utf-8'),
            value='%'.join([str(begin_time), str(end_time)]).encode('utf-8')
        )


async def get_kafka():
    yield Kafka(kafka_settings.topic)
