from enum import Enum

from pydantic_settings import BaseSettings
from pydantic import field_validator, ValidationError


class EnvType(Enum):
    DEV = "dev"
    PROD = "prod"
    TEST = "test"


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @field_validator("ENVIRONMENT")
    def validate_environment(cls, value):
        if value not in EnvType._value2member_map_:
            raise ValidationError(f"Invalid environment: {value}")

        return value
