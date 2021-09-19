from pydantic import BaseSettings
from pydantic.networks import PostgresDsn
from pydantic.networks import PostgresDsn

DEFAULT_VERSION = "v1beta1"
DEFAULT_PREFIX = "api"


class AsyncPostgresDsn(PostgresDsn):
    default_scheme = "postgresql+asyncpg"
    allowed_schemes = {"postgresql+asyncpg", "postgres+asyncpg"}


class Config(BaseSettings):
    DATABASE_URI: PostgresDsn
    API_PREFIX: str = DEFAULT_PREFIX
    version: str = DEFAULT_VERSION

    @property
    def ASYNC_DATABASE_URI(self) -> AsyncPostgresDsn:
        ASYNC_DATABASE_URI = self.DATABASE_URI.replace("postgresql://", "postgresql+asyncpg://")
        return ASYNC_DATABASE_URI


config = Config()

