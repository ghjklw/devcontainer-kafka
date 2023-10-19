from kafka import KafkaProducer
from pydantic import BaseModel
from typing import TypeVar, Generic

from devcontainer_kafka.config import KafkaConfiguration

T = TypeVar("T", bound=BaseModel)

class KafkaPydanticProducer(Generic[T]):
    def __init__(self, config: KafkaConfiguration):
        self._producer = KafkaProducer(
            bootstrap_servers=[f"{config.host}:{config.port}"],
            value_serializer=self.serialize
        )

    def serialize(self, data: T) -> bytes:
        return data.model_dump_json().encode("utf-8")

    def send(self, data: T):
        self._producer.send(topic=type(data).__name__, value=data) # pyright: ignore[reportUnknownMemberType]
