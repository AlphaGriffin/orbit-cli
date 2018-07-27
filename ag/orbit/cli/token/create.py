#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.ops.create import Create
from ag.orbit.cli import arg
from ag.orbit.cli.network import broadcast
#from ag.orbit.wallet import key


def run(args):
    args = None if args is not None and len(args) < 1 else args

    print("Create new token...")

    if args is not None:
        if len(args) < 3 or len(args) > 6:
            print()
            raise ValueError("Expecting no less than 3 and no more than 6 arguments")

    supply = int(arg(args, 0, "Supply"))
    decimals = int(arg(args, 1, "Decimals"))
    symbol = arg(args, 2, "Symbol")
    name = arg(args, 3, "Name", True)
    main_uri = arg(args, 4, "Main URI", True)
    image_uri = arg(args, 5, "Image URI", True)

    op = Create(supply, decimals, symbol, name, main_uri, image_uri)
    broadcast(op)


if __name__ == '__main__':
    from contextlib import suppress
    from sys import argv

    with suppress(KeyboardInterrupt):
        try:
            print()
            run(argv[1:] if len(argv) > 1 else None)

        except (ValueError, TypeError) as e:
            print()
            print("{}: {}".format(argv[0], e))

