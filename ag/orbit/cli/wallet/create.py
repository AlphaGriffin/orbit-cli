#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.command import main
from ag.orbit.cli import password_handler
from ag.orbit.wallet import path, create as wcreate


def run(args):
    if args is not None and len(args) > 2:
        raise ValueError("Expecting no more than 2 arguments")

    name = args[0].strip() if args is not None and len(args) > 0 else None
    password = args[1] if args is not None and len(args) > 1 else None

    if name is not None and not name:
        raise ValueError("Name cannot be empty")

    print()
    create(name, password)

def create(name=None, password=None):
    if name:
        print("Creating new ORBIT wallet file for BCH...")
    else:
        print("Generating new BCH key-pair...")

    if name:
        print("    Name: {}".format(name))
        wpath = path(name)
        print("    File: {}".format(wpath))

    else:
        wpath = None

    def show_address(address):
        print("    Public BCH address: {}".format(address))

    def unencrypted_warning():
        print("WARNING: You are about to save the private key without encryption! THIS IS NOT RECOMMENDED.")
        confirm = input("    Please type 'confirm' if you accept the risk and wish to continue: ")

        if confirm != 'confirm':
            raise ValueError('User abort')

    wallet = wcreate(wpath, None, password_handler(password, create=True), show_address, unencrypted_warning)

    if name is None:
        print("    Private BCH key (hex): {}".format(wallet.to_hex()))

    else:
        print()
        print("Wallet saved")

    return wallet


if __name__ == '__main__':
    main(run)

