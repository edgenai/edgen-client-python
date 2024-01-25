

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types.misc import Version

__all__ = ["Misc"]

class Misc(SyncAPIResource):
    @cached_property
    def version(self) -> Version:
        return EdgenVersion(self._client)

class EdgenVersion(SyncAPIResource):
    def create(self) -> Version:
        return self._get(
            "/misc/version",
            cast_to=Version,
        )
