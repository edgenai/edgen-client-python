from ..._base_client import (
    make_request_options,
)

from typing import overload
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import EdgenStatus

__all__ = ["CompletionsStatus"]

class CompletionsStatus(SyncAPIResource):
    def create(self) -> EdgenStatus:
        return self._get(
            "/chat/completions/status",
            cast_to=EdgenStatus,
        )

      
