# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit import API
#from ag.orbit.ops.address import Address
from ag.orbit.cli.wallet.list import list as list_wallets
from ag.orbit.cli.wallet.key import key as get_key

from bitcash import Key
from bitcash.exceptions import InsufficientFunds
from bitcash.network import get_fee
from bitcash.transaction import MESSAGE_LIMIT

from sys import stdin
from getpass import getpass
from time import sleep


#MESSAGE_LIMIT = 35

# TODO: support self-signing

def broadcast(op, token_address=None):
    orbit = API()

    '''
    messages = orbit.prepare(op, limit=MESSAGE_LIMIT)

    for message in messages:
        if len(message) > MESSAGE_LIMIT:
            raise AssertionError("The data is too large")

    # sanity check
    if orbit.parse(b''.join(messages), combined=True) != op:
        raise AssertionError('Re-parsing the prepared bytes of this operation does not return the same values')
    '''

    interactive = True

    if not stdin.isatty():
        key = stdin.readline().rstrip()
        interactive = False

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

    print("Loading wallet...")
    wallet = Key.from_hex(key[0])
    print("    Your Address: {}".format(wallet.address))
    print("    Balance: {} satoshi".format(wallet.get_balance()))

    print("    Unspents:")
    for unspent in wallet.unspents:
        print("        {}".format(unspent))
    print("        {} unspent transaction{}".format(len(wallet.unspents), "" if len(wallet.unspents) == 1 else "s"))

    print()
    print("Preparing transaction...")
    if not token_address:
        token_address = wallet.address
    print("    Token Address: {}".format(token_address))

    try:
        message = orbit.prepare(token_address, op)
    except InvalidAddress as e:
        raise ValueError("An invalid bitcoincash address was entered")

    #print(message)

    if len(message) > MESSAGE_LIMIT:
        raise AssertionError("The data is too large")

    # sanity check
    parsed = orbit.parse(message)
    if parsed != (token_address, op):
        #print(parsed)
        raise AssertionError('Re-parsing the prepared bytes of this operation does not return the same values')

    '''
    sig = Address.sign(wallet, token_address)
    token = Address(token_address, wallet.public_key, sig)
    token_messages = orbit.prepare(token, limit=MESSAGE_LIMIT)

    for token_message in token_messages:
        if len(token_message) > MESSAGE_LIMIT:
            raise AssertionError("The token address data is too large")

    # sanity check
    if orbit.parse(b''.join(token_messages), combined=True) != token:
        raise AssertionError('Re-parsing the prepared bytes of the token address operation does not return the same values')
    '''

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
        print("------------------------------------------")
        print("CAREFULLY REVIEW THE FOLLOWING TRANSACTION")
        print("------------------------------------------")
        print()

    print("    Signer's Address:")
    print("        {}".format(wallet.address))

    print()
    print("    Token Address:")
    print("        {}".format(token_address))

    print()
    #print("    {}".format(token.__str__('        ')))
    print("    {}".format(op.__str__('        ')))

    print()
    print("    Fee/byte: {} satoshi".format(fee))

    if interactive:
        print()

        confirm = input("    Type 'confirm' if you are sure you want to broadcast this transaction: ")

        if confirm != "confirm":
            raise ValueError("User abort")

    # TODO: attempt broadcast through ORBIT node first, use bitcash wallet as fallback

    print()
    #print("Waiting 60 seconds to broadcast (rate limit?)...")
    #sleep(60)

    #token_messages.extend(messages)
    #print(token_messages)

    try:
        print("Broadcasting...")
        #tx = wallet.send([], fee=fee, message=token_messages)
        tx = wallet.send([], fee=fee, message=message)
        print('Transaction: {}'.format(tx))
        return tx

    except ConnectionError as e:
        raise ValueError("Unable to broadcast, try again later or try increasing the fee: {}".format(e))

    except InsufficientFunds as e:
        raise ValueError(e)

