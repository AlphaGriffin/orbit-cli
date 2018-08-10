#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.command import main
from ag.orbit.ops.allocation import Create
from ag.orbit.cli import arg
from ag.orbit.cli.network import broadcast


def run(args):
    args = args if args else None

    print()
    print("Create new token...")

    if args:
        if len(args) < 3 or len(args) > 6:
            print()
            raise ValueError("Expecting no less than 3 and no more than 6 arguments")

    supply = int(arg(args, 0, "Supply"))
    decimals = int(arg(args, 1, "Decimals"))
    symbol = arg(args, 2, "Symbol")
    name = arg(args, 3, "Name", optional=True)
    main_uri = arg(args, 4, "Main URI", optional=True)
    image_uri = arg(args, 5, "Image URI", optional=True)

    create(supply, decimals, symbol, name, main_uri, image_uri)

def create(supply, decimals, symbol, name=None, main_uri=None, image_uri=None):
    op = Create(supply, decimals, symbol, name, main_uri, image_uri)
    broadcast(op)


if __name__ == '__main__':
    main(run)

