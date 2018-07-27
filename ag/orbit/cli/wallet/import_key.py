#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit import API
from ag.orbit.cli.config import dir
from ag.orbit.cli.encryption import encrypt

from os.path import exists, join
from base64 import urlsafe_b64encode
from sys import stdin
from getpass import getpass

from bitcash.wallet import PrivateKey


def run(args):
    if args is None or len(args) < 1 or len(args) > 3:
        raise ValueError("Expecting no less than 1 and no more than 3 arguments")

    name = args[0].strip()
    key = args[1] if len(args) > 1 else None
    password = args[2] if len(args) > 2 else None

    if not name:
        raise ValueError("Name cannot be empty")

    import_key(name, key, password)

def import_key(name, key=None, password=None):
    print("Importing Bitcoin Cash key for new wallet file...")

    print("    Name: {}".format(name))
    path = join(dir, urlsafe_b64encode(name.encode('utf-8')).decode('ascii') + ".wallet")
    print("    File: {}".format(path))

    if exists(path):
        print()
        raise ValueError("A wallet file by this name already exists! Please delete it first.")

    if key is None:
        if stdin.isatty():
            print()
            key = getpass("Enter private key (hex): ")

        else:
            key = stdin.readline().rstrip()

    if not key:
        print()
        raise ValueError("Key may not be empty")

    try:
        wallet = PrivateKey.from_hex(key)
    except ValueError:
        print()
        raise ValueError("Not a valid key")

    print("    Public address: {}".format(wallet.address))

    if password is None:
        print()

        if stdin.isatty():
            password = getpass("Enter password for encryption: ")

            if password:
                confirm = getpass("Please re-enter your password: ")

                if password != confirm:
                    print()
                    raise ValueError("The passwords do not match")

            else:
                print("WARNING: You are about to save the private key without encryption! This is not recommended.")
                confirm = input("    Please type 'confirm' if you accept the risk and wish to continue: ")

                if confirm != 'confirm':
                    print()
                    raise ValueError("User abort")

        else:
            password = stdin.readline().rstrip()

            #if not password:
            #    raise ValueError("Password may not be empty")

    elif not password:
        print()
        raise ValueError("Password may not be empty")

    key = key.encode('charmap')
    print()

    if password:
        data = b"%E%" + encrypt(API.PREAMBLE + key, password.encode('utf-8'))
    else:
        print("WARNING: Saving key without encryption.")
        data = b"%D%" + key

    with open(path, 'wb') as out:
        out.write(data)

    print("Wallet saved")


if __name__ == '__main__':
    from contextlib import suppress
    from sys import argv

    with suppress(KeyboardInterrupt):
        run(argv[1:])

