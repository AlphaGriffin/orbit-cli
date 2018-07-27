# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

#import ag.logging as log

from os import mkdir, path

from appdirs import AppDirs
dirs = AppDirs("orbit-cli", "Alpha Griffin")

dir = dirs.user_config_dir
#log.debug("Starting up", configdir=dir)

if not path.exists(dir):
    #log.info("Running first-time setup for configuration...")

    #log.debug("Creating user config directory")
    mkdir(dir)

if not path.isdir(dir):
    #log.fatal("Expected a directory for configdir", configdir=dir)
    raise Exception("Not a directory: " + dir)
