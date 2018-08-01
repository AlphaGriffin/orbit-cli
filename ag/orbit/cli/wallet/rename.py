#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.command import main
from ag.orbit.wallet import path

import os


def run(args):
    if args is None or len(args) != 2:
        raise ValueError("Expecting exactly 2 arguments")

    name = args[0].strip()
    newname = args[1].strip()

    if not name or not newname:
        raise ValueError("Names cannot be empty")

    if name == newname:
        raise ValueError("New name must be different than original name")

    print()
    rename(name, newname)

def rename(name, newname):
    print("Renaming ORBIT wallet file...")

    print("    Original name: {}".format(name))
    wpath = path(name)
    print("    Original file: {}".format(wpath))

    if not os.path.exists(wpath):
        raise ValueError("Wallet does not exist")

    print("    New name: {}".format(newname))
    newwpath = path(newname)
    print("    New file: {}".format(newwpath))

    if os.path.exists(newwpath):
        raise ValueError("A wallet already exists with the new name")

    os.rename(wpath, newwpath)
    print()
    print("Wallet renamed")


if __name__ == '__main__':
    main(run)

