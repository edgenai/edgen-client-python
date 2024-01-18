

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .transcriptions import (
    Transcriptions,
    AsyncTranscriptions,
    TranscriptionsWithRawResponse,
    AsyncTranscriptionsWithRawResponse,
)

__all__ = ["Audio", "AsyncAudio"]


class Audio(SyncAPIResource):
    @cached_property
    def transcriptions(self) -> Transcriptions:
        return Transcriptions(self._client)

    @cached_property
    def with_raw_response(self) -> AudioWithRawResponse:
        return AudioWithRawResponse(self)


class AsyncAudio(AsyncAPIResource):
    @cached_property
    def transcriptions(self) -> AsyncTranscriptions:
        return AsyncTranscriptions(self._client)


class AudioWithRawResponse:
    def __init__(self, audio: Audio) -> None:
        self.transcriptions = TranscriptionsWithRawResponse(audio.transcriptions)


class AsyncAudioWithRawResponse:
    def __init__(self, audio: AsyncAudio) -> None:
        self.transcriptions = AsyncTranscriptionsWithRawResponse(audio.transcriptions)
