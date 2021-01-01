import asyncio
import io
import os
import json
from apiclient import discovery
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.errors import HttpError
from httplib2 import HttpLib2Error
from pydantic import BaseModel, Field

from .base import ResourceFetcher
from ..exceptions import ResourceFetchError


class GoogleDocExtraInfo(BaseModel):
    file_id: str = Field(
        ..., description="The google drive id of the file to download."
    )
    export_type: str = Field(
        "application/pdf", description="The mime type of the export."
    )


class GoogleDocExportFetcher(ResourceFetcher):
    def validate_settings(self):
        return super().validate_settings()

    async def fetch(self) -> bool:
        credentials = self._load_google_creds_from_env()

        event_loop = asyncio.get_event_loop()

        # download asynchronously in another thread
        export_data = await event_loop.run_in_executor(
            None, self._download_exported_doc, credentials
        )

    @staticmethod
    def _load_google_creds_from_env() -> service_account.Credentials:
        credentials_info = os.getenv("GOOGLE_SERVICE_USER_CREDENTIALS")

        if not credentials_info:
            raise ResourceFetchError(
                "Could not read credentials info from the environment. GOOGLE_SERVICE_USER_CREDENTIALS must "
                "be set equal to the json config of the service user. "
                "Hint: (`export GOOGLE_SERVICE_USER_CREDENTIALS=$(cat google_creds.json)`)"
            )

        return service_account.Credentials.from_service_account_info(
            json.loads(credentials_info)
        )

    def _download_exported_doc(self, credentials: service_account.Credentials):
        try:
            service = discovery.build("drive", "v3", credentials=credentials)
            request = service.files().export_media(
                fileId=self.settings.file_id, mimeType=self.settings.export_type
            )
            document_bytes = io.BytesIO()
            downloader = MediaIoBaseDownload(document_bytes, request)

            done = False
            while done is False:
                _, done = downloader.next_chunk()
        except HttpError as e:
            raise ResourceFetchError(
                f"There was an error fetching the exported file: {e}"
            ) from e

        except HttpLib2Error as e:
            raise ResourceFetchError(
                f"There was an error communicating with the Google Drive API: {e}"
            ) from e

        return document_bytes
