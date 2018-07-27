# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

#import ag.logging as log


def usage():
    print()
    print("Usage: orbit-cli token <command>")
    print()
    print("Where <command> is:")
    print("    help")
    print("        Display this usage screen")
    print()
    print("    create <supply> <decimals> <symbol> [<name>] [<main_uri>] [<image_uri>]")
    print("        Create new token")
    print("            - <supply> is initial token supply (number of indivisible units)")
    print("            - <decimals> is number of decimal points to divide up the supply")
    print("            - <symbol> is ticker symbol")
    print("            - <name> is optional name")
    print("            - <main_uri> is optional link to a web page, etc.")
    print("            - <image_uri> is optional link or data for embedded image")
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

from sys import argv, exit
from contextlib import suppress

with suppress(KeyboardInterrupt):
    call = 'orbit-cli token'

    if len(argv) > 1 and argv[1] is None:
        # we were called from the parent module
        args = argv[2:]
    else:
        args = argv[1:]

    if len(args) < 1:
        usage()
        exit(1)

    cmd = args[0]
    args = args[1:] if len(args) > 1 else None
        
    if cmd == 'help':
        usage()

    elif cmd == 'create':
        print()

        if args is not None and (len(args) < 3 or len(args) > 6):
            print("{} {}: wrong number of arguments".format(call, cmd))
            exit(2)

        from .create import run
        try:
            run(args)

        except (ValueError, TypeError) as e:
            print()
            print("{} {}: {}".format(call, cmd, e))
            exit(3)

    else:
        #log.error("unknown command", command=cmd)
        print()
        print("{}: unknown command: {}".format(call, cmd))
        usage()
        exit(2)

