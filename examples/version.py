#!/usr/bin/env python

import sys
sys.path.append("/home/ts/binedge/wrk/client/edgen-python-client/src") 


from edgen import Edgen

client = Edgen()

def main() -> None:
    # Create transcription from audio file
    ver = client.misc.version.create()
    print(ver)

if __name__ == "__main__":
    main()
