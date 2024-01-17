# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from edgen import Edgen, AsyncEdgen
from tests.utils import assert_matches_type
from edgen._client import Edgen, AsyncEdgen
from edgen.types.chat import ChatCompletion

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:3000/v1")
api_key = "My API Key"

@pytest.mark.skip(reason="currently not working for missing features in edgen") 
class TestCompletions:
    strict_client = Edgen(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Edgen(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create_overload_1(self, client: Edgen) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="gpt-3.5-turbo",
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Edgen) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                    "name": "string",
                }
            ],
            model="gpt-3.5-turbo",
            frequency_penalty=-2,
            function_call="none",
            functions=[
                {
                    "description": "string",
                    "name": "string",
                    "parameters": {"foo": "bar"},
                }
            ],
            logit_bias={"foo": 0},
            logprobs=True,
            max_tokens=0,
            n=1,
            presence_penalty=-2,
            response_format={"type": "json_object"},
            seed=-9223372036854776000,
            stop="string",
            stream=False,
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
            ],
            top_logprobs=0,
            top_p=1,
            user="user-1234",
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Edgen) -> None:
        response = client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="gpt-3.5-turbo",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    def test_method_create_overload_2(self, client: Edgen) -> None:
        client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="gpt-3.5-turbo",
            stream=True,
        )

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Edgen) -> None:
        client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                    "name": "string",
                }
            ],
            model="gpt-3.5-turbo",
            stream=True,
            frequency_penalty=-2,
            function_call="none",
            functions=[
                {
                    "description": "string",
                    "name": "string",
                    "parameters": {"foo": "bar"},
                }
            ],
            logit_bias={"foo": 0},
            logprobs=True,
            max_tokens=0,
            n=1,
            presence_penalty=-2,
            response_format={"type": "json_object"},
            seed=-9223372036854776000,
            stop="string",
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
            ],
            top_logprobs=0,
            top_p=1,
            user="user-1234",
        )

    @parametrize
    def test_raw_response_create_overload_2(self, client: Edgen) -> None:
        response = client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="gpt-3.5-turbo",
            stream=True,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        response.parse()

@pytest.mark.skip(reason="currently not working for missing features in edgen") 
class TestAsyncCompletions:
    strict_client = AsyncEdgen(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncEdgen(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create_overload_1(self, client: AsyncEdgen) -> None:
        completion = await client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="gpt-3.5-turbo",
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, client: AsyncEdgen) -> None:
        completion = await client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                    "name": "string",
                }
            ],
            model="gpt-3.5-turbo",
            frequency_penalty=-2,
            function_call="none",
            functions=[
                {
                    "description": "string",
                    "name": "string",
                    "parameters": {"foo": "bar"},
                }
            ],
            logit_bias={"foo": 0},
            logprobs=True,
            max_tokens=0,
            n=1,
            presence_penalty=-2,
            response_format={"type": "json_object"},
            seed=-9223372036854776000,
            stop="string",
            stream=False,
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
            ],
            top_logprobs=0,
            top_p=1,
            user="user-1234",
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, client: AsyncEdgen) -> None:
        response = await client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="gpt-3.5-turbo",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    async def test_method_create_overload_2(self, client: AsyncEdgen) -> None:
        await client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="gpt-3.5-turbo",
            stream=True,
        )

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, client: AsyncEdgen) -> None:
        await client.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                    "name": "string",
                }
            ],
            model="gpt-3.5-turbo",
            stream=True,
            frequency_penalty=-2,
            function_call="none",
            functions=[
                {
                    "description": "string",
                    "name": "string",
                    "parameters": {"foo": "bar"},
                }
            ],
            logit_bias={"foo": 0},
            logprobs=True,
            max_tokens=0,
            n=1,
            presence_penalty=-2,
            response_format={"type": "json_object"},
            seed=-9223372036854776000,
            stop="string",
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
            ],
            top_logprobs=0,
            top_p=1,
            user="user-1234",
        )

    @parametrize
    async def test_raw_response_create_overload_2(self, client: AsyncEdgen) -> None:
        response = await client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="gpt-3.5-turbo",
            stream=True,
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        response.parse()
