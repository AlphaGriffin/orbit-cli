#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit import API
from ag.orbit.cli.config import dir
from ag.orbit.cli.encryption import encrypt, decrypt

from os.path import exists, join
from base64 import urlsafe_b64encode
from sys import stdin
from getpass import getpass


def run(args):
    if args is None or len(args) < 1 or len(args) > 2:
        raise ValueError("Expecting no less than 1 and no more than 2 arguments")

    name = args[0].strip()
    password = args[1] if len(args) > 1 else None

    key(name, password)

def key(name, password=None, display=True):
    print("Reading key from Bitcoin Cash wallet...")

    print("    Name: {}".format(name))
    path = join(dir, urlsafe_b64encode(name.encode('utf-8')).decode('ascii') + ".wallet")
    print("    File: {}".format(path))

    if not exists(path):
        raise ValueError("A wallet by this name does not exist")

    with open(path, 'rb') as fin:
        data = fin.read()

    if len(data) < 4:
        raise ValueError("Not a valid wallet file")

    if data.startswith(b'%E%'):
        encrypted = True
    elif data.startswith(b'%D%'):
        encrypted = False
    else:
        raise ValueError("Not a valid wallet file")

    data = data[3:]

    if encrypted:
        if password is None:
            if stdin.isatty():
                password = getpass("    Enter password for decryption: ")

            else:
                password = stdin.readline().rstrip()

        if not password:
            raise ValueError("Password may not be empty")

        key = decrypt(data, password.encode('utf-8'))

        if not key.startswith(API.PREAMBLE):
            raise ValueError("Password is not correct")

        key = key[len(API.PREAMBLE):]

    else:
        key = data
        
    key = key.decode('charmap')

    if display:
        print()
        print("    Private key (hex): {}".format(key))

    return key


if __name__ == '__main__':
    from contextlib import suppress
    from sys import argv

    with suppress(KeyboardInterrupt):
        run(argv[1:])


