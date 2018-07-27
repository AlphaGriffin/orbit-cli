#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.cli.config import dir

from os.path import join, split
from base64 import urlsafe_b64decode
from glob import glob


def run():
    print("Listing wallets at {}".format(dir))

    wallets = glob(join(dir, "*.wallet"))

    for filename in wallets:
        filename = split(filename)[1][:-7]
        name = urlsafe_b64decode(filename).decode('utf-8')
        print("    '{}'".format(name))

    print()
    print("{} wallet{} found".format(len(wallets), "s" if len(wallets) != 1 else ""))


if __name__ == '__main__':
    from contextlib import suppress
    from sys import argv

    with suppress(KeyboardInterrupt):
        run()

