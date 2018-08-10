# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

#import ag.logging as log

from ...command import invoke

from sys import argv, exit
from contextlib import suppress


CALL = 'orbit-cli admin'

def usage():
    print()
    print("Usage: {} <command>".format(CALL))
    print()
    print("    Token administration.")
    print()
    print("Where <command> is:")
    print("    help")
    print("        Display this usage screen")
    print()
    print("    create [<supply> <decimals> <symbol> [<name> [<main_uri> [<image_uri>]]]]")
    print("        Create new token")
    print("            - <supply> is initial token supply (number of indivisible units)")
    print("            - <decimals> is number of decimal points to divide up the supply")
    print("            - <symbol> is ticker symbol")
    print("            - <name> is optional name")
    print("            - <main_uri> is optional link to a web page, etc.")
    print("            - <image_uri> is optional link or data for embedded image")
    print()
    print("    transfer [<to> <units|ALL>]")
    print("        Transfer tokens")
    print("            - <to> is the address to transfer to")
    print("            - <units> is the number of indivisible units (not normalized) to transfer;")
    print("                the text \"ALL\" may be used to transfer all available tokens")
    print()
    print("    advertise [<exchange_rate> <units_avail> <units_min> <units_max> <block_begin>")
    print("              <block_end> <block_deliver> [<preregister>]]")
    print("        Set up an automated crowd-sale or faucet")
    print("            - <exchange_rate> is the price in satoshi for a single indivisible token unit;")
    print("                a negative number indicates fractional value (e.g. -5 = 1/5 i.e. 5 units per satoshi);")
    print("                the text \"NONE\" indicates free exchange (faucet)")
    print("            - <units_avail> is the number of units to make available (this supply will be locked);")
    print("                use \"ALL\" to make all available;")
    #print("                use \"ANY\" to make all available without dedicating them (i.e. no supply locking)")
    print("            - <units_min> is the minimum units a single user (address) shall receive;")
    print("                the text \"NONE\" indicates no minimum")
    print("            - <units_max> is the maximum units a singe user (address) shall receive;")
    print("                the text \"NONE\" indicates no maximum")
    print("            - <block_begin> is the block height when the crowd-sale or faucet becomes active;")
    print("                use \"NOW\" to begin as soon as soon as the transaction is confirmed (next block)")
    print("            - <block_end> is the block height when the crowd-sale or faucet closes;")
    print("                use \"FOREVER\" to remain active until supply runs out")
    print("            - <block_deliver> is the first block when tokens will be delivered;")
    print("                use \"ANY\" for immediate delivery")
    print("            - <preregister>, if present, indicates that users are allowed to register before <block_begin>;")
    print("                only valid when using both <exchange_rate> and <block_begin>;")
    print("                crowd-sale payments are still only accepted no sooner than <block_begin>;")
    print("                payments sent with an early registration are simply ignored;")
    print("                must be an affirmative boolean value: \"TRUE\", \"YES\", or \"Y\"")
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
        exit(401)

    cmd = args[0]
    args = args[1:] if len(args) > 1 else None
        
    if cmd == 'help':
        usage()

    elif cmd == 'create':
        from .create import run
        invoke(CALL, cmd, 402, run, args, 3, 6, optional=True)

    elif cmd == 'transfer':
        from .transfer import run
        invoke(CALL, cmd, 403, run, args, 2, 2, optional=True)

    elif cmd == 'advertise':
        from .advertise import run
        invoke(CALL, cmd, 404, run, args, 7, 8, optional=True)

    else:
        #log.error("unknown command", command=cmd)
        print()
        print("{}: unknown command: {}".format(CALL, cmd))
        usage()
        exit(499)

