#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.command import main
from ag.orbit.cli import password_handler
from ag.orbit.wallet import path, create as wcreate

from sys import stdin
from getpass import getpass


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
    print("Importing private BCH key for new ORBIT wallet file...")

    print("    Name: {}".format(name))
    wpath = path(name)
    print("    File: {}".format(wpath))

    def get_key():
        nonlocal key

        if not key:
            if stdin.isatty():
                print()
                key = getpass("Enter private BCH key (hex): ")

            else:
                key = stdin.readline().rstrip()

        if not key:
            print()
            raise ValueError("Key may not be empty")

        return key

    def show_address(address):
        print("    Public BCH address: {}".format(address))

    def unencrypted_warning():
        print("WARNING: You are about to save the private key without encryption! THIS IS NOT RECOMMENDED.")
        confirm = input("    Please type 'confirm' if you accept the risk and wish to continue: ")

        if confirm != 'confirm':
            raise ValueError('User abort')

    wallet = wcreate(wpath, get_key, password_handler(password, create=True), show_address, unencrypted_warning)

    print()
    print("Wallet saved")

    return wallet


if __name__ == '__main__':
    main(run)

