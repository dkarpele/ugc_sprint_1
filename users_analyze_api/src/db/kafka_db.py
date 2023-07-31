from kafka import KafkaProducer, KafkaConsumer

from users_analyze_api.src.core.config import kafka_settings


class Kafka:
    def __init__(self, topic: str):
        self.topic = topic
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=kafka_settings.bootstrap_servers,
            security_protocol="SASL_SSL",
            sasl_mechanism="SCRAM-SHA-512",
            sasl_plain_username=kafka_settings.user,
            sasl_plain_password=kafka_settings.password,
            ssl_cafile=kafka_settings.ssl_cafile)
        self.producer = KafkaProducer(
            bootstrap_servers=kafka_settings.bootstrap_servers,
            security_protocol="SASL_SSL",
            sasl_mechanism="SCRAM-SHA-512",
            sasl_plain_username=kafka_settings.user,
            sasl_plain_password=kafka_settings.password,
            ssl_cafile=kafka_settings.ssl_cafile
        )

    def create_post(self, user_id: str, movie_id: str, begin_time, end_time):
        self.producer.send(
            topic=self.topic,
            value=' '.join([str(begin_time), str(end_time)]).encode('utf-8'),
            key=' '.join([str(user_id), str(movie_id)]).encode('utf-8')
        )


async def get_kafka():
    yield Kafka('views')
