#!/usr/bin/env python

from edgen import Edgen

client = Edgen()

def main() -> None:
    status = client.chat.completions.status.create()

    print(f"Chat Completions Status")
    print(f"=======================")
    print(f"active model: {status.active_model}")
    print(f"download    : {status.download_ongoing}")
    print(f"progress    : {status.download_progress}")
    print(f"errors      : {status.last_errors}")

    status = client.audio.transcriptions.status.create()

    print(f"Audio Transcriptions Status")
    print(f"=======================")
    print(f"active model: {status.active_model}")
    print(f"download    : {status.download_ongoing}")
    print(f"progress    : {status.download_progress}")
    print(f"errors      : {status.last_errors}")

if __name__ == "__main__":
    main()
