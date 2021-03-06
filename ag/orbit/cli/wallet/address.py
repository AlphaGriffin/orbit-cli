#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.command import main
from ag.orbit.cli import password_handler
from ag.orbit.wallet import path, access


def run(args):
    if args is None or len(args) < 1 or len(args) > 2:
        raise ValueError("Expecting no less than 1 and no more than 2 arguments")

    name = args[0].strip()
    password = args[1] if len(args) > 1 else None

    print()
    address(name, password)

def address(name, password=None, display=True):
    print("Reading BCH address from ORBIT wallet file...")

    print("    Name: {}".format(name))
    wpath = path(name)
    print("    File: {}".format(wpath))

    wallet = access(wpath, password_handler(password))

    if display:
        print()
        print("    Public BCH address: {}".format(wallet.address))

    return wallet.address


if __name__ == '__main__':
    main(run)

