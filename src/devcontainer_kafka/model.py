from pydantic import BaseModel
from polyfactory.factories.pydantic_factory import ModelFactory

class Person(BaseModel):
    name: str
    age: float
    height: float
    weight: float

class PersonFactory(ModelFactory[Person]):
    __model__ = Person
