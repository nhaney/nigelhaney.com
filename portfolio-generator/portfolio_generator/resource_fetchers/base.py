from abc import ABC, abstractmethod

#  from ..settings import PortfolioResource


class ResourceFetcher(ABC):
    def __init__(self, settings) -> None:
        self.settings = settings

    @abstractmethod
    def validate_settings(self):
        ...

    @abstractmethod
    async def fetch(self):
        ...
