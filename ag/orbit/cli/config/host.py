#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.command import main
from ag.orbit.cli.config import get_orbit_host, set_orbit_host


def run(args):
    if args and len(args) != 1:
        raise ValueError("Expecting exactly 1 argument")

    if args:
        host = args[0]

        print()
        print("    Setting ORBIT node hostname / IP address to: {}".format(host))

        orbit = set_orbit_host(host)

        print()
        print("ORBIT host saved to: {}".format(orbit))

    else:
        host = get_orbit_host()

        print()
        print("    Hostname / IP address for ORBIT node: {}".format(host))


if __name__ == '__main__':
    main(run)

