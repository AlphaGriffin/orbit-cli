#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.command import main
from ag.orbit.ops.allocation import Transfer
from ag.orbit.cli import arg
from ag.orbit.cli.network import broadcast


def run(args):
    args = args if args else None

    print()
    print("Transfer tokens...")

    if args:
        if len(args) != 2:
            print()
            raise ValueError("Expecting exactly 2 arguments")

    to = arg(args, 0, "Destination address")

    units = arg(args, 1, "Number of indivisible units (leave blank to transfer ALL tokens)", optional=True)
    if units and units != "ALL":
        units = int(units)

    transfer(to, units)

def transfer(to, units):
    if units == "ALL":
        units = None

    op = Transfer(to, units)
    broadcast(op)


if __name__ == '__main__':
    main(run)

