# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

#import ag.logging as log

from sys import argv, exit
from contextlib import suppress


CALL = 'orbit-cli'

def usage():
    print()
    print("Usage: {} <module>".format(CALL))
    print()
    print("Where <module> is:")
    print("    help     - Display this usage screen")
    print("    token    - Token commands")
    print("    wallet   - Wallet commands")
    #print("    network  - Network commands")
    print()


with suppress(KeyboardInterrupt):
    args = argv[1:]

    if len(args) < 1:
        usage()
        exit(1)

    argv[1] = None # a hack so sub-modules can tell if they were invoked from here, or directly
    module = args[0]
    #args = args[1:] if len(args) > 1 else None
        
    if module == 'help':
        usage()

    elif module == 'token':
        from .token import __main__

    elif module == 'wallet':
        from .wallet import __main__

    #elif module == 'network':
    #    from .network import __main__

    else:
        #log.error("unknown module", module=module)
        print()
        print("{}: unknown module: {}".format(CALL, module))
        usage()
        exit(99)

