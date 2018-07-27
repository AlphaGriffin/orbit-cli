# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from .wallet.list import run as list_wallets
from .wallet.key import key as get_key
from ag.orbit import API

from bitcash import Key, __version__
from bitcash.exceptions import InsufficientFunds
from bitcash.network import get_fee
from bitcash.transaction import MESSAGE_LIMIT

from sys import stdin
from getpass import getpass
from time import sleep


# TODO: support self-signing

def broadcast(op):
    api = API()
    message = api.prepare(op)

    print(len(message))
    
    if len(message) > MESSAGE_LIMIT:
        raise ValueError("The data is too large. Try reducing some text or removing optional data.")

    # sanity check
    if api.parse(message) != op:
        raise AssertionError('Re-parsing the prepared bytes of this operation does not return the same values')

    interactive = True

    if not stdin.isatty():
        key = stdin.readline().rstrip()
        interactive = False
        fee = None

    else:
        print()
        value = False

        while not value:
            value = input("    Enter wallet name (leave blank to list), '@' for private key: ") # TODO: "or '!' to self-sign"

            if not value:
                print()
                list_wallets()
                print()

            elif value == '@':
                value = getpass("    Enter private key (hex): ")

                if value:
                    key = value

            #elif value == '!':
            #    self = True
            #    confirm = False

            else:
                print()
                try:
                    key = get_key(value, display=False)

                except ValueError as e:
                    print()
                    print("Sorry: {}".format(e))
                    value = False

                print()

    print("Preparing transaction...")
    wallet = Key.from_hex(key)
    print("    From/to: {}".format(wallet.address))
    print("    Balance: {} satoshi".format(wallet.get_balance()))

    print("    Unspents:")
    for unspent in wallet.unspents:
        print("        {}".format(unspent))
    print("        {} unspent transaction{}".format(len(wallet.unspents), "" if len(wallet.unspents) == 1 else "s"))

    fee = get_fee()
    #fee = 1

    if interactive:
        print()
        print("    Enter fee per byte in satoshi ({} is currently recommended),".format(fee))
        userfee = input ("        leave blank to use the recommended fee: ")

        if userfee:
            fee = int(userfee)
            if fee < 1:
                raise ValueError('Fee must be at least 1 satoshi')

        print()
        print("----------------------------------------")
        print("CAREFULLY REVIEW THE FOLLOWING OPERATION")
        print("----------------------------------------")
        print()

    print("    Fee/byte: {} satoshi".format(fee))
    print("    {}".format(op.__str__('        ')))

    if interactive:
        print()

        confirm = input("    Type 'confirm' if you are sure you want to broadcast this transaction: ")

        if confirm != "confirm":
            raise ValueError("User abort")

    # TODO: attempt broadcast through ORBIT node first, use bitcash wallet as fallback

    print()
    #print("Waiting 60 seconds to broadcast (rate limit?)...")
    #sleep(60)

    try:
        print("Broadcasting...")
        tx = wallet.send([], fee=fee, message=message)
        print('Transaction: {}'.format(tx))
        return tx
    except ConnectionError as e:
        raise ValueError("Unable to broadcast, try again later or try increasing the fee: {}".format(e))
    except InsufficientFunds as e:
        raise ValueError(e)

