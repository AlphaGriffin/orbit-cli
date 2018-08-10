# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

#import ag.logging as log

from ...command import invoke

from sys import argv, exit
from contextlib import suppress


CALL = 'orbit-cli token'

def usage():
    print()
    print("Usage: {} <command>".format(CALL))
    print()
    print("    User token management.")
    print()
    print("Where <command> is:")
    print("    help")
    print("        Display this usage screen")
    print()
    print("    transfer [<token> <to> <units|ALL>]")
    print("        Transfer tokens")
    print("            - <token> is the token address")
    print("            - <to> is the address to transfer to")
    print("            - <units> is the number of indivisible units (not normalized) to transfer;")
    print("                the text \"ALL\" may be used to transfer all available tokens")
    print()
    print("    register [<token>]")
    print("        Register interest in crowd-sale or faucet")
    print("            - <token> is the token address")
    print()
    print("    unregister [<token>]")
    print("        Remove interest in crowd-sale or faucet")
    print("            - <token> is the token address")
    print()
    print("All commands may be called without arguments for full interactive mode.")
    print()
    print("Most commands require a private key for signing messages. You will be prompted")
    print("to open a saved wallet or enter a key when required, and to confirm the transaction.")
    print()
    print("However, a private key may be piped in from stdin for non-interactive usage.")
    print("Supplying a key in this manner will auto-calculate a fee and not ask for confirmation;")
    print("USE WITH CAUTION.")
    print()

with suppress(KeyboardInterrupt):
    if len(argv) > 1 and argv[1] is None:
        # we were called from the parent module
        args = argv[2:]
    else:
        args = argv[1:]

    if len(args) < 1:
        usage()
        exit(301)

    cmd = args[0]
    args = args[1:] if len(args) > 1 else None
        
    if cmd == 'help':
        usage()

    elif cmd == 'transfer':
        from .transfer import run
        invoke(CALL, cmd, 302, run, args, 3, 6, optional=True)

    elif cmd == 'register':
        from .register import run
        invoke(CALL, cmd, 303, run, args, 1, 1, optional=True)

    elif cmd == 'unregister':
        from .unregister import run
        invoke(CALL, cmd, 304, run, args, 1, 1, optional=True)

    else:
        #log.error("unknown command", command=cmd)
        print()
        print("{}: unknown command: {}".format(CALL, cmd))
        usage()
        exit(399)

