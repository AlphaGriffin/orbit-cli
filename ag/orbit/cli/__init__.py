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


def arg(args, index, name, optional=False, description=None, hints=None, none=None):
    value = None

    if args and len(args) > index:
        value = args[index]

    elif args is None or not optional:
        if description or hints:
            print("    {}:".format(name))
            if description:
                print("        {}".format(description))
            if hints:
                for hint in hints:
                    print("          * {}".format(hint))
            value = input("      --> ")
        else:
            value = input("    {}: ".format(name))

    if not optional and not value:
        raise ValueError("{} is required".format(name))

    if none and value == none:
        return None
    else:
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

