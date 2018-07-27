# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

#import ag.logging as log


def usage():
    print()
    print("Usage: orbit-cli <module>")
    print()
    print("Where <module> is:")
    print("    help     - Display this usage screen")
    print("    token    - Token commands")
    print("    wallet   - Wallet commands")
    print()

from sys import argv, exit
from contextlib import suppress

with suppress(KeyboardInterrupt):
    if len(argv) < 2:
        usage()
        exit(1)
        
    elif argv[1] == 'help':
        usage()

    elif argv[1] == 'token':
        argv[1] = None
        from .token import __main__

    elif argv[1] == 'wallet':
        argv[1] = None
        from .wallet import __main__

    else:
        #log.error("unknown module", module=argv[1])
        print()
        print("orbit-cli: unknown module: " + argv[1])
        usage()
        exit(2)

