# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from edgen import Edgen, AsyncEdgen
from tests.utils import assert_matches_type
from edgen._client import Edgen, AsyncEdgen
from edgen.types.audio import Transcription

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:3000/v1")
api_key = "My API Key"

@pytest.mark.skip(reason="not working because of codec") 
class TestTranscriptions:
    strict_client = Edgen(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Edgen(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Edgen) -> None:
        transcription = client.audio.transcriptions.create(
            file=b"raw file contents",
            model="whisper-1",
        )
        assert_matches_type(Transcription, transcription, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Edgen) -> None:
        transcription = client.audio.transcriptions.create(
            file=b"raw file contents",
            model="whisper-1",
            language="string",
            prompt="string",
            response_format="json",
            temperature=0,
        )
        assert_matches_type(Transcription, transcription, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Edgen) -> None:
        response = client.audio.transcriptions.with_raw_response.create(
            file=b"raw file contents",
            model="whisper-1",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcription = response.parse()
        assert_matches_type(Transcription, transcription, path=["response"])


@pytest.mark.skip(reason="not working because of codec") 
class TestAsyncTranscriptions:
    strict_client = AsyncEdgen(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncEdgen(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncEdgen) -> None:
        transcription = await client.audio.transcriptions.create(
            file=b"raw file contents",
            model="whisper-1",
        )
        assert_matches_type(Transcription, transcription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncEdgen) -> None:
        transcription = await client.audio.transcriptions.create(
            file=b"raw file contents",
            model="whisper-1",
            language="string",
            prompt="string",
            response_format="json",
            temperature=0,
        )
        assert_matches_type(Transcription, transcription, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncEdgen) -> None:
        response = await client.audio.transcriptions.with_raw_response.create(
            file=b"raw file contents",
            model="whisper-1",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcription = response.parse()
        assert_matches_type(Transcription, transcription, path=["response"])
