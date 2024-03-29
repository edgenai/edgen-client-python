#!/usr/bin/env python

from edgen import Edgen

client = Edgen()

def main() -> None:
    ver = client.misc.version.create()

    build = ''
    if len(ver.build) > 0:
       build = '-' + ver.build
 
    print(f"Edgen Version is {ver.major}.{ver.minor}.{ver.patch}{build}")

if __name__ == "__main__":
    main()
