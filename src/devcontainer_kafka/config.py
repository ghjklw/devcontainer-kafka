from pydantic import BaseModel
from pydantic_settings import BaseSettings

class KafkaConfiguration(BaseModel):
    host: str = "kafka"
    port: int = 9092

class Configuration(BaseSettings):
    """Global settings."""
    kafka: KafkaConfiguration = KafkaConfiguration()
