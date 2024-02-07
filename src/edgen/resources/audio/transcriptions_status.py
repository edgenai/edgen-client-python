from ..._base_client import (
    make_request_options,
)

from typing import overload
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import EdgenStatus

__all__ = ["TranscriptionsStatus"]

class TranscriptionsStatus(SyncAPIResource):
    def create(self) -> EdgenStatus:
        return self._get(
            "/audio/transcriptions/status",
            cast_to=EdgenStatus,
        )

      
