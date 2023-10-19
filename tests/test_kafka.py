import pytest

from typing import TypeVar
from pydantic import BaseModel

from devcontainer_kafka.config import Configuration
from devcontainer_kafka.model import Person, PersonFactory
from devcontainer_kafka.producer import KafkaPydanticProducer
from devcontainer_kafka.consumer import KafkaPydanticConsumer

T = TypeVar("T", bound=BaseModel)

@pytest.fixture()
def person() -> Person:
    return PersonFactory.build()

@pytest.fixture()
def config() -> Configuration:
    return Configuration()

def test_send_receive(
        config: Configuration,
        person: Person,
    ):
        consumer = KafkaPydanticConsumer[Person](config=config.kafka, model=Person, group_id="PyTestConsumer")
        producer = KafkaPydanticProducer[Person](config=config.kafka)

        producer.send(person)

        next(consumer.receive())
