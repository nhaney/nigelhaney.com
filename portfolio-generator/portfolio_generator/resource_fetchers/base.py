from abc import ABC, abstractmethod
from pathlib import Path
from typing import Iterator, Type
from portfolio_generator.exceptions import ResourceFetchError

import pydantic

from ..settings import PortfolioResource


class ResourceFetcher(ABC):
    extra_config_cls: Type[pydantic.BaseModel]

    def __init__(self, settings) -> None:
        self.settings = settings

        try:
            self.fetcher_config = self.extra_config_cls(**self.settings)
        except pydantic.ValidationError as e:
            raise ResourceFetchError(
                "Could not initialize resource fetcher of type {resource_type}: {e}"
            ) from e

    @abstractmethod
    async def fetch(self) -> Iterator[Path]:
        ...
