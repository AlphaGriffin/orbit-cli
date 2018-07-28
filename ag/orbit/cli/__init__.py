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


def arg(args, index, name, optional=False):
    value = None

    if args is None:
        value = input("    {}: ".format(name))

    elif len(args) > index:
        value = args[index]

    elif not optional:
        value = input("    {}: ".format(name))

    return value if value else None

