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
    if args is not None and len(args) > 2:
        raise ValueError("Expecting no more than 2 arguments")

    name = args[0].strip() if args is not None and len(args) > 0 else None
    password = args[1] if args is not None and len(args) > 1 else None

    if name is not None and not name:
        raise ValueError("Name cannot be empty")

    #if password is not None and not password:
    #    raise ValueError("Password cannot be empty")

    create(name, password)

def create(name=None, password=None):
    print("Creating new Bitcoin Cash wallet...")

    if name is not None:
        print("    Name: {}".format(name))
        path = join(dir, urlsafe_b64encode(name.encode('utf-8')).decode('ascii') + ".wallet")
        print("    File: {}".format(path))

        if exists(path):
            raise ValueError("A wallet file by this name already exists! Please delete it first.")

    wallet = PrivateKey()
    print("    Public address: {}".format(wallet.address))
    key = wallet.to_hex()

    if name is None:
        print("    Private key (hex): {}".format(wallet.to_hex()))
        return

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

            if not password:
                raise ValueError("Password may not be empty")

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

