import os
from pathlib import Path

import yaml
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerConfig(BaseModel):
    host: str = Field(default="127.0.0.1")
    port: int = Field(default=8000, ge=1, le=65535)


class Config(BaseSettings):
    server: ServerConfig = ServerConfig()

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )

    @classmethod
    def from_yaml(cls, yaml_file: str) -> "Config":
        with Path(yaml_file).open() as file:
            yaml_data = yaml.safe_load(file)
        return cls(**yaml_data)


def load_config() -> "Config":
    env = os.getenv("ENVIRONMENT", "default")
    config_path = f"config/{env}.yaml"
    return Config.from_yaml(config_path)
