# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os as _os
from typing_extensions import override

from . import types
from ._types import NoneType, Transport, ProxiesTypes
from ._utils import file_from_path
from ._client import Client, Edgen, Stream, Timeout, Transport, AsyncClient, AsyncEdgen, AsyncStream, RequestOptions
from ._version import __title__, __version__
from ._exceptions import (
    APIError,
    EdgenError,
    ConflictError,
    NotFoundError,
    APIStatusError,
    RateLimitError,
    APITimeoutError,
    BadRequestError,
    APIConnectionError,
    AuthenticationError,
    InternalServerError,
    PermissionDeniedError,
    UnprocessableEntityError,
    APIResponseValidationError,
)
from ._utils._logs import setup_logging as _setup_logging

__all__ = [
    "types",
    "__version__",
    "__title__",
    "NoneType",
    "Transport",
    "ProxiesTypes",
    "EdgenError",
    "APIError",
    "APIStatusError",
    "APITimeoutError",
    "APIConnectionError",
    "APIResponseValidationError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "UnprocessableEntityError",
    "RateLimitError",
    "InternalServerError",
    "Timeout",
    "RequestOptions",
    "Client",
    "AsyncClient",
    "Stream",
    "AsyncStream",
    "Edgen",
    "AsyncEdgen",
    "file_from_path",
]

from .version import VERSION as VERSION

_setup_logging()

# Update the __module__ attribute for exported symbols so that
# error messages point to this module instead of the module
# it was originally defined in, e.g.
# edgen._exceptions.NotFoundError -> edgen.NotFoundError
__locals = locals()
for __name in __all__:
    if not __name.startswith("__"):
        try:
            __locals[__name].__module__ = "edgen"
        except (TypeError, AttributeError):
            # Some of our exported symbols are builtins which we can't set attributes for.
            pass

# ------ Module level client ------
import typing as _t
import typing_extensions as _te

import httpx as _httpx

from ._base_client import DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES

api_key: str | None = None

organization: str | None = None

base_url: str | _httpx.URL | None = None

timeout: float | Timeout | None = DEFAULT_TIMEOUT

max_retries: int = DEFAULT_MAX_RETRIES

default_headers: _t.Mapping[str, str] | None = None

default_query: _t.Mapping[str, object] | None = None

http_client: _httpx.Client | None = None

_ApiType = _te.Literal["edgen"]

api_type: _ApiType | None = _t.cast(_ApiType, _os.environ.get("EDGEN_API_TYPE"))

api_version: str | None = _os.environ.get("EDGEN_API_VERSION")

class _ModuleClient(Edgen):
    # Note: we have to use type: ignores here as overriding class members
    # with properties is technically unsafe but it is fine for our use case

    @property  # type: ignore
    @override
    def api_key(self) -> str | None:
        return api_key

    @api_key.setter  # type: ignore
    def api_key(self, value: str | None) -> None:  # type: ignore
        global api_key

        api_key = value

    @property  # type: ignore
    @override
    def organization(self) -> str | None:
        return organization

    @organization.setter  # type: ignore
    def organization(self, value: str | None) -> None:  # type: ignore
        global organization

        organization = value

    @property
    @override
    def base_url(self) -> _httpx.URL:
        if base_url is not None:
            return _httpx.URL(base_url)

        return super().base_url

    @base_url.setter
    def base_url(self, url: _httpx.URL | str) -> None:
        super().base_url = url  # type: ignore[misc]

    @property  # type: ignore
    @override
    def timeout(self) -> float | Timeout | None:
        return timeout

    @timeout.setter  # type: ignore
    def timeout(self, value: float | Timeout | None) -> None:  # type: ignore
        global timeout

        timeout = value

    @property  # type: ignore
    @override
    def max_retries(self) -> int:
        return max_retries

    @max_retries.setter  # type: ignore
    def max_retries(self, value: int) -> None:  # type: ignore
        global max_retries

        max_retries = value

    @property  # type: ignore
    @override
    def _custom_headers(self) -> _t.Mapping[str, str] | None:
        return default_headers

    @_custom_headers.setter  # type: ignore
    def _custom_headers(self, value: _t.Mapping[str, str] | None) -> None:  # type: ignore
        global default_headers

        default_headers = value

    @property  # type: ignore
    @override
    def _custom_query(self) -> _t.Mapping[str, object] | None:
        return default_query

    @_custom_query.setter  # type: ignore
    def _custom_query(self, value: _t.Mapping[str, object] | None) -> None:  # type: ignore
        global default_query

        default_query = value

    @property  # type: ignore
    @override
    def _client(self) -> _httpx.Client:
        return http_client or super()._client

    @_client.setter  # type: ignore
    def _client(self, value: _httpx.Client) -> None:  # type: ignore
        global http_client

        http_client = value

_client: Edgen | None = None

def _load_client() -> Edgen:  # type: ignore[reportUnusedFunction]
    global _client

    if _client is None:
        global api_type, api_version

        if api_version is None:
            api_version = _os.environ.get("EDGEN_API_VERSION")

        _client = _ModuleClient(
            api_key=api_key,
            organization=organization,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
            default_query=default_query,
            http_client=http_client,
        )
        return _client

    return _client


def _reset_client() -> None:  # type: ignore[reportUnusedFunction]
    global _client

    _client = None


from ._module_client import (
    chat as chat,
    audio as audio,
    misc as misc,
)
