#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

import ag.orbit.cli
from ag.orbit.command import main
from ag.orbit.config import dir
from ag.orbit.wallet import list as get_list


def run(args):
    if args is not None and len(args) != 0:
        raise ValueError("Not expecting any arguments")

    print()
    list()

def list():
    print("Listing wallets at {}".format(dir))

    wallets = get_list()

    for wallet in wallets:
        print("    '{}'".format(wallet))

    print()
    print("{} wallet{} found".format(len(wallets), "s" if len(wallets) != 1 else ""))


if __name__ == '__main__':
    main(run)

