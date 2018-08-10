#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.command import main
from ag.orbit.cli.config import get_orbit_port, set_orbit_port


def run(args):
    if args and len(args) != 1:
        raise ValueError("Expecting exactly 1 argument")

    if args:
        port = args[0]

        print()
        print("    Setting ORBIT node port number to: {}".format(port))

        orbit = set_orbit_port(port)

        print()
        print("ORBIT port saved to: {}".format(orbit))

    else:
        port = get_orbit_port()

        print()
        print("    Port number for ORBIT node: {}".format(port))


if __name__ == '__main__':
    main(run)

