#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.command import main
from ag.orbit.cli import password_handler
from ag.orbit.wallet import path, access

from bitcash.base58 import b58encode

from base64 import b64encode


def run(args):
    if args is None or len(args) < 1 or len(args) > 2:
        raise ValueError("Expecting no less than 1 and no more than 2 arguments")

    name = args[0].strip()
    password = args[1] if len(args) > 1 else None

    print()
    key(name, password)

def key(name, password=None, display=True):
    print("Reading BCH private key from ORBIT wallet...")

    print("    Name: {}".format(name))
    wpath = path(name)
    print("    File: {}".format(wpath))

    wallet = access(wpath, password_handler(password))
    key_hex = wallet.to_hex()
    key_bytes = wallet.to_bytes()
    key_der = wallet.to_der()
    key_pem = wallet.to_pem()
    key_int = wallet.to_int()
    key_wif = wallet.to_wif()

    if display:
        print()
        print("    Private BCH key (bytes): {}".format(key_bytes))
        print("    Private BCH key (base58): {}".format(b58encode(key_bytes)))
        print("    Private BCH key (hex): {}".format(key_hex))
        #print("    Private BCH key (hex base58): {}".format(b58encode(key_hex)))
        print("    Private BCH key (der): {}".format(key_der))
        print("    Private BCH key (der base58): {}".format(b58encode(key_der)))
        print("    Private BCH key (der base64): {}".format(b64encode(key_der)))
        print("    Private BCH key (pem): {}".format(key_pem))
        print("    Private BCH key (int): {}".format(key_int))
        print("    Private BCH key (wif): {}".format(key_wif))

    return (key_hex, key_bytes, key_der, key_pem, key_int)


if __name__ == '__main__':
    main(run)

