from abc import ABC, abstractmethod

from ..settings import PortfolioResource


class ResourceFetcher(ABC):
    resource_name: str = ""

    def __init__(self, settings: PortfolioResource) -> None:
        self.settings = settings

    @abstractmethod
    def validate_settings(self):
        ...

    @abstractmethod
    async def fetch(self):
        ...
