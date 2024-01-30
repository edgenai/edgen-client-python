# Edgen Python API library

The Edgen Python is a clone of the official OpenAI Python library.
It provides convenient access to the Edgen REST API from any Python 3.7+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

The original library was generated from the [OpenAPI specification](https://github.com/openai/openai-openapi) with [Stainless](https://stainlessapi.com/).

## Documentation

The API documentation can be found [here](https://docs.edgen.co).

## Installation

```sh
pip install edgen
```

## Usage

The full API of this library can be found in [api.md](https://www.github.com/edgenai/edgen-client-python/blob/main/api.md).

```python
import os
from edgen import Edgen

client = Edgen(
    base_url=os.environ.get("EDGEN_BASE_URL"), # this is default and can be omitted
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="ignore",
)
```

Note that, in the current version, the model is ignored.
The model per endpoint is chosen in the _edgen-server_.
However, the _model_ element must be present for compatibility with the OpenAI spec.

## Async usage

Simply import `AsyncEdgen` instead of `Edgen` and use `await` with each API call:

```python
import os
import asyncio
from edgen import AsyncEdgen

client = AsyncEdgen()

async def main() -> None:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="ignore",
    )


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## Streaming Responses

We provide support for streaming responses using Server Side Events (SSE).

```python
from edgen import Edgen

client = Edgen()

stream = client.chat.completions.create(
    model="ignore",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
```

The async client uses the exact same interface.

```python
from edgen import AsyncEdgen

client = AsyncEdgen()


async def main():
    stream = await client.chat.completions.create(
        model="ignore",
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True,
    )
    async for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")


asyncio.run(main())
```

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev), which provide helper methods for things like:

- Serializing back into JSON, `model.model_dump_json(indent=2, exclude_unset=True)`
- Converting to a dictionary, `model.model_dump(exclude_unset=True)`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

# Remove `await` for non-async usage.

````

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from edgen import Edgen

client = Edgen()

completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Can you generate an example json object describing a fruit?",
        }
    ],
    model="ignore",
    response_format={"type": "json_object"},
)
````

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `edgen.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `edgen.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `edgen.APIError`.

```python
import edgen
from edgen import Edgen

client = Edgen()

try:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="ignore",
    )
except edgen.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except edgen.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except edgen.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from edgen import Edgen

# Configure the default for all requests:
client = Edgen(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "How can I get the name of the current day in Node.js?",
        }
    ],
    model="ignore",
)
```

### Timeouts

By default requests time out after 10 minutes. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration) object:

```python
from edgen import Edgen

# Configure the default for all requests:
client = Edgen(
    # 20 seconds (default is 10 minutes)
    timeout=20.0,
)

# More granular control:
client = Edgen(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5 * 1000).chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "How can I list all files in a directory using Python?",
        }
    ],
    model="gpt-3.5-turbo",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `EDGEN_LOG` to `debug`.

```shell
$ export EDGEN_LOG=debug
```

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call.

```py
from edgen import Edgen

client = Edgen()
response = client.chat.completions.with_raw_response.create(
    messages=[{
        "role": "user",
        "content": "Say this is a test",
    }],
    model="ignore",
)
print(response.headers.get('X-My-Header'))

completion = response.parse()  # get the object that `chat.completions.create()` would have returned
print(completion)
```

These methods return an [`APIResponse`](https://github.com/edgenai/edgen-client-python/tree/main/src/edgen/_response.py) object.

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for proxies
- Custom transports
- Additional [advanced](https://www.python-httpx.org/advanced/#client-instances) functionality

```python
import httpx
from edgen import Edgen

client = Edgen(
    # Or use the `EDGEN_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions.

## Requirements

Python 3.7 or higher.

## Tests

The tests are based on _pytest_ with the _pytest-asyncio_, _anyio_, _Faker_ and _respx_ plugins.
