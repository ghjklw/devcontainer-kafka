from kafka import KafkaConsumer
from kafka.consumer.fetcher import ConsumerRecord
from pydantic import BaseModel
from typing import TypeVar, Generic, Generator, Iterator

from devcontainer_kafka.config import KafkaConfiguration

T = TypeVar("T", bound=BaseModel)

class KafkaPydanticConsumer(Generic[T]):
    def __init__(self, config: KafkaConfiguration, model: type[T], group_id: str | None = None):
        self._model = model
        self._consumer: Iterator[ConsumerRecord] = KafkaConsumer(
            model.__name__,
            bootstrap_servers=[f"{config.host}:{config.port}"],
            group_id=group_id,
            auto_offset_reset="earliest",
            value_deserializer=self.deserialize,
        )

    def deserialize(self, data: bytes) -> T:
        return self._model.model_validate_json(data.decode("utf-8"))

    def receive_with_metadata(self) -> Generator[ConsumerRecord, None, None]:
        for data in self._consumer:
            yield data

    def receive(self) -> Generator[T, None, None]:
        for data in self._consumer:
            yield data.value # pyright: ignore[reportUnknownMemberType]
