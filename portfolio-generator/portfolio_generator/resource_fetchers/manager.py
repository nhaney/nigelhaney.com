import asyncio
from typing import List

from pydantic.error_wrappers import ValidationError

from ..settings import ResourceSetting
from . import RESOURCE_TYPE_FETCHERS
from .base import ResourceFetcher


class ResourceFetcherManager:
    """Initializes fetchers based on a list of resource configurations passed in."""

    def __init__(self, resource_settings: List[ResourceSetting]):
        self._fetchers: List[ResourceFetcher] = []

        for resource_setting in resource_settings:
            try:
                fetcher = RESOURCE_TYPE_FETCHERS[resource_setting.resource_type](
                    resource_setting
                )
            except ValidationError:
                raise ResourceFetcherInitializationError(
                    f"Error initializing fetcher for resource: {resource_setting.name}"
                )

            self._fetchers.append(fetcher)

    def run(self):
        asyncio.run(self._run_fetchers())

    async def _run_fetchers(self):
        tasks = []

        for fetcher in self._fetchers:
            tasks.append(fetcher.fetch())

        results = await asyncio.gather(*tasks, return_exceptions=True)

