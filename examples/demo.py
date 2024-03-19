#!/usr/bin/env -S poetry run python

from edgen import Edgen

client = Edgen()

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model="default",
    messages=[
        {
            "role": "user",
            "content": "what is 1 + 2?",
        },
    ],
)
print(completion)

# Streaming:
print("----- streaming request -----")
stream = client.chat.completions.create(
    model="default",
    messages=[
        {
            "role": "user",
            "content": "what is the result of 1+2?",
        },
    ],
    stream=True,
)
for chunk in stream:
    if not chunk.choices:
        continue

    print(chunk.choices[0].delta.content, end="")
print()
