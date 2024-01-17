#!/usr/bin/env python

from pathlib import Path

import sys
sys.path.append("/home/ts/binedge/wrk/client/edgen-python-client/src") 


from edgen import Edgen

edgen = Edgen()

speech_file_path = Path(__file__).parent.parent.parent.parent / "audio" / "frost.wav"


def main() -> None:
    # Create transcription from audio file
    transcription = edgen.audio.transcriptions.create(model="whisper-1", file=speech_file_path)
    print(transcription)

if __name__ == "__main__":
    main()
