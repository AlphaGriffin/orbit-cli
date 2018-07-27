===========================================================================
ORBIT CLI - Command-Line Interface for Op_Return Bitcoin-Implemented Tokens
===========================================================================

**A command-line interface for interacting with tokens on Bitcoin Cash implementing the ORBIT standard.**

The official website for ORBIT is http://orbit.cash.

.. contents:: Table of Contents
.. toctree::
   API Documentation <api/modules>

*"Orbit the moon"*


Introduction
------------

The ORBIT CLI is a program that allows interaction with and management of tokens on Bitcoin Cash implementing the ORBIT standard.

ORBIT CLI is open source and licensed under the MIT license. See the `LICENSE <LICENSE>`_ file for more details.


The ORBIT Ecosystem
~~~~~~~~~~~~~~~~~~~

ORBIT is a specification for simple, fungible tokens implemented by utilizing OP_RETURN for the storage of token events on the Bitcoin Cash blockchain. No changes to the Bitcoin Cash protocol or nodes are required. However, wallets may wish to incorporate this token standard in order to allow the user to easily take account of and interact with tokens that adhere to this ORBIT standard.

The following projects, when used in conjunction with ORBIT CLI, complete a full ecosystem for tokens on Bitcoin Cash using ORBIT:

- ORBIT Specification and API: https://github.com/AlphaGriffin/orbit
- ORBIT Node: https://github.com/AlphaGriffin/orbit-node
- ORBIT Qt Wallet: https://github.com/AlphaGriffin/orbit-wallet
- ORBIT Web: https://github.com/AlphaGriffin/orbit-web


Specification
-------------

The ORBIT repository at https://github.com/AlphaGriffin/orbit defines the official and complete specification for ORBIT. 

*The current specification version is: 0 (beta testing). Version 0 is reserved and should be used for all testing.*


ORBIT CLI
---------

This ORBIT CLI is written in Python.


Dependencies
~~~~~~~~~~~~

- Python 3
- ORBIT API: https://github.com/AlphaGriffin/orbit
- appdirs: https://github.com/ActiveState/appdirs (`pip install appdirs`)
- BitCash >= 0.5.2.4: https://github.com/sporestack/bitcash (`pip install bitcash\>=0.5.2.4`)
- PyCrypto: https://github.com/dlitz/pycrypto (`pip install pycrypto`)

In addition to the above, ORBIT CLI may require RPC access to a local or remote ORBIT node for some operations, such as the one provided by Alpha Griffin (http://orbit.alphagriffin.com).


Build Overview
~~~~~~~~~~~~~~

Both a Makefile and setup.py are provided and used. The setup.py uses Python's standard setuptools package and you can call this script directly to do the basic Python tasks such as creating a wheel, etc.

The most common project build tasks are all provided in the Makefile. To see the full list of project targets::

    make help

Sphinx is used to generate html documentation and man pages. All documentation (html as well as man pages) may be regenerated at any time with::

    make docs

Every so often, when new source class files are created or moved, you will want to regenerate the API documentation templates. These templates may be modified by hand so this task does not overwrite existing files; you'll need to remove any existing files from ``api/`` that you want recreated. Then generate the API templates and re-build all documentation as follows::

    make apidoc
    make docs

There's not much to do for a simple Python project but your build may want to do more. In any case you can call ``make python`` if you need to (in orbit this target simply delegates to ``./setup.py build``).

Build all the common tasks (including documentation) as follows::

    make all

To clean up all the common generated files from your project folder::

    make clean


Installing
~~~~~~~~~~

To install this project to the local system::

    make install

Note that you may need superuser permissions to perform the above step.


Using
~~~~~

**FIXME**

