#!/usr/bin/env python

from pathlib import Path

from edgen import Edgen

edgen = Edgen()

speech_file_path = Path(__file__).parent / "audio" / "frost.wav"

def main() -> None:
    transcription = edgen.audio.transcriptions.create(model="whisper-1", file=speech_file_path)
    print(transcription)

if __name__ == "__main__":
    main()
