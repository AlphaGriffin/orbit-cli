# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

#import ag.logging as log


def usage():
    print()
    print("Usage: orbit-cli wallet <command>")
    print()
    print("Where <command> is:")
    print("    help")
    print("        Display this usage screen")
    print()
    print("    create [<name> [<password>]]")
    print("        Create new wallet and save or display the private key")
    print("            - <name> is a simple label under which to save the wallet key;")
    print("                if omitted, the key is displayed on screen and the wallet is not saved")
    print()
    print("    import <name> [<key> [<password>]]")
    print("        Import existing key and save as a wallet file")
    print("            - <name> is a simple label under which to save the wallet key")
    print("            - <key> is the private key (hex) to import")
    print("            - If piping <key> and <password> from stdin they should be separated by newline")
    print()
    print("    list")
    print("        List all saved wallets")
    print()
    print("    address <name> [<password>]")
    print("        Print the public address for a wallet")
    print("            - <name> is the name of the wallet to read")
    print("            - <password> is the encryption password used during creation")
    print()
    print("    key <name> [<password>]")
    print("        Print the private key stored in a wallet")
    print("            - <name> is the name of the wallet to read")
    print("            - <password> is the encryption password used during creation")
    print()
    print("The <key> or <password> used by any of these commands may be provided on the command line")
    print("or piped in through stdin. If omitted, you will be prompted to enter the key/password.")
    print()

from sys import argv, exit
from contextlib import suppress

with suppress(KeyboardInterrupt):
    if len(argv) > 1 and argv[1] is None:
        # we were called from the parent module
        argv = argv[1:]

    if len(argv) < 2:
        usage()
        exit(1)
        
    elif argv[1] == 'help':
        usage()

    elif argv[1] == 'create':
        print()

        if len(argv) > 4:
            print("orbit-cli wallet create: wrong number of arguments")
            exit(2)

        from .create import run
        try:
            run(argv[2:])

        except ValueError as e:
            print()
            print("orbit-cli wallet create: {}".format(e))
            exit(2)

    elif argv[1] == 'import':
        print()

        if len(argv) < 3 or len(argv) > 5:
            print("orbit-cli wallet import: wrong number of arguments")
            exit(3)

        from .import_key import run
        try:
            run(argv[2:])

        except ValueError as e:
            print()
            print("orbit-cli wallet import: {}".format(e))
            exit(3)

    elif argv[1] == 'list':
        print()

        if len(argv) != 2:
            print("orbit-cli wallet list: not expecting any arguments")
            exit(4)

        from .list import run
        try:
            run()

        except ValueError as e:
            print()
            print("orbit-cli wallet list: {}".format(e))
            exit(4)

    elif argv[1] == 'address':
        print()

        if len(argv) < 3 or len(argv) > 4:
            print("orbit-cli wallet address: wrong number of arguments")
            exit(5)

        from .address import run
        try:
            run(argv[2:])

        except ValueError as e:
            print()
            print("orbit-cli wallet address: {}".format(e))
            exit(5)

    elif argv[1] == 'key':
        print()

        if len(argv) < 3 or len(argv) > 4:
            print("orbit-cli wallet key: wrong number of arguments")
            exit(6)

        from .key import run
        try:
            run(argv[2:])

        except ValueError as e:
            print()
            print("orbit-cli wallet key: {}".format(e))
            exit(6)

    else:
        #log.error("unknown command", command=argv[1])
        print()
        print("orbit-cli wallet: unknown command: " + argv[1])
        usage()
        exit(2)

