#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.command import main
from ag.orbit.cli import password_handler
from ag.orbit.cli.config import get_orbit_host, get_orbit_port
from ag.orbit.wallet import path, access
from ag.orbit.webapi import Client, Endpoints

from decimal import Decimal


def run(args):
    if args is None or len(args) < 1 or len(args) > 2:
        raise ValueError("Expecting no less than 1 and no more than 2 arguments")

    name = args[0].strip()
    password = args[1] if len(args) > 1 else None

    print()
    tokens(name, password)

def tokens(name, password=None):
    print("Opening wallet...")

    print("    Name: {}".format(name))
    wpath = path(name)
    print("    File: {}".format(wpath))

    wallet = access(wpath, password_handler(password))

    print()
    print("Connecting to ORBIT node to retrieve token information...")

    host = get_orbit_host()
    port = get_orbit_port()

    print("    Host: {}".format(host))
    print("    Port: {}".format(port))

    client = Client(host=host, port=port)
    tokens = client.get_user_tokens(wallet.address)[Endpoints.USER_TOKENS]

    if tokens:
        for token in tokens:
            print()
            print("    Token @ {}".format(token['address']))
            print("        Name: {}".format(token['name']))
            print("        Symbol: {}".format(token['symbol']))
            decimals = token['decimals']
            print("        Decimals: {}".format(decimals))
            print("      Balance")
            total = token['units']
            print("          Total: {} ({} unit{})".format(
                Decimal(total).scaleb(-1 * decimals), total, "" if total == 1 else "s"))
            available = token['available']
            print("          Available: {} ({} unit{})".format(
                Decimal(available).scaleb(-1 * decimals), available, "" if available == 1 else "s"))
    else:
        print()
        print("    No tokens")


if __name__ == '__main__':
    main(run)

