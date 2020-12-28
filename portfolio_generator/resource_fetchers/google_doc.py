from .base import ResourceFetcher


class GoogleDocFetcher(ResourceFetcher):
    def validate_settings(self):
        return super().validate_settings()

    async def fetch(self):
        return super().fetch()
