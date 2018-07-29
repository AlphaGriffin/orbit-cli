# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

#import ag.logging as log

from ...command import invoke

from sys import argv, exit
from contextlib import suppress


CALL = 'orbit-cli wallet'

def usage():
    print()
    print("Usage: {} <command>".format(CALL))
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
    print("    balance <name> [<password>]")
    print("        Print the current balance for a wallet")
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

    elif cmd == 'create':
        from .create import run
        invoke(CALL, cmd, 302, run, args, 0, 2)

    elif cmd == 'import':
        from .import_key import run
        invoke(CALL, cmd, 303, run, args, 1, 3)

    elif cmd == 'list':
        from .list import run
        invoke(CALL, cmd, 304, run, args)

    elif cmd == 'address':
        from .address import run
        invoke(CALL, cmd, 305, run, args, 1, 2)

    elif cmd == 'balance':
        from .balance import run
        invoke(CALL, cmd, 306, run, args, 1, 2)

    elif cmd == 'key':
        from .key import run
        invoke(CALL, cmd, 307, run, args, 1, 2)

    else:
        #log.error("unknown command", command=cmd)
        print()
        print("{}: unknown command: {}".format(CALL, cmd))
        usage()
        exit(399)

