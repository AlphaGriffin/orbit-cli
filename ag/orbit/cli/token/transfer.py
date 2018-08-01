#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.command import main
from ag.orbit.ops.transfer import Transfer
from ag.orbit.cli import arg
from ag.orbit.cli.network import broadcast


def run(args):
    args = args if args else None

    print()
    print("Transfer tokens...")

    if args:
        if len(args) != 3:
            print()
            raise ValueError("Expecting exactly 3 arguments")

    token = arg(args, 0, "Token address (leave blank to use your wallet address)")
    to = arg(args, 1, "Destination address")

    units = arg(args, 2, "Number of indivisible units (leave blank to transfer ALL tokens)")
    if units and units != "ALL":
        units = int(units)

    transfer(token, to, units)

def transfer(token, to, units):
    if units == "ALL":
        units = None

    op = Transfer(to, units)
    broadcast(op, token_address=token)


if __name__ == '__main__':
    main(run)

