# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

"""Command-Line Interface for ORBIT

This is a command-line interface following the ORBIT specification
defined at https://github.com/AlphaGriffin/orbit

.. module:: ag.orbit.cli
   :platform: Unix
   :synopsis: Command-Line Interface for ORBIT
.. moduleauthor:: Shawn Wilson <lannocc@alphagriffin.com>
"""

from .__version__ import __version__
print ("ORBIT Command-Line Interface version %s" % (__version__))

#import ag.logging as log
#log.set(log.INFO)

from sys import stdin
from getpass import getpass


def arg(args, index, name, optional=False):
    value = None

    if args is None:
        value = input("    {}: ".format(name))

    elif len(args) > index:
        value = args[index]

    elif not optional:
        value = input("    {}: ".format(name))

    return value if value else None


def password_handler(password=None, create=False):
    def get_password():
        nonlocal password

        if password is not None:
            pass

        elif stdin.isatty():
            print()
            password = getpass("Enter password for {}: ".format('encryption' if create else 'decryption'))

            if create and password:
                confirm = getpass("Please re-enter your password: ")

                if password != confirm:
                    raise ValueError("The passwords do not match")

        else:
            password = stdin.readline().rstrip()

        return password

    return get_password

