# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

#import ag.logging as log

from os import makedirs, path

from appdirs import AppDirs
dirs = AppDirs("orbit-cli", "Alpha Griffin")

dir = dirs.user_config_dir
#log.debug("Starting up", configdir=dir)

if not path.exists(dir):
    #log.info("Running first-time setup for configuration...")

    #log.debug("Creating user config directory")
    makedirs(dir, exist_ok=True)

if not path.isdir(dir):
    #log.fatal("Expected a directory for configdir", configdir=dir)
    raise Exception("Not a directory: " + dir)


def get_orbit_host():
    orbit = path.join(dir, 'orbit_host')

    if not path.exists(orbit):
        #raise ValueError('ORBIT node hostname / IP address not set. You must set a host first with: `orbit-cli config host`')
        return 'localhost'

    with open(orbit, 'r') as orbitin:
        return orbitin.readline()

def set_orbit_host(host):
    orbit = path.join(dir, 'orbit_host')
    with open(orbit, 'w') as out:
        out.write(host)

    return orbit


def get_orbit_port():
    orbit = path.join(dir, 'orbit_port')

    if not path.exists(orbit):
        #raise ValueError('ORBIT node port number not set. You must set a port first with: `orbit-cli config port`')
        from ag.orbit.webapi import DEFAULT_PORT
        return DEFAULT_PORT

    with open(orbit, 'r') as orbitin:
        return int(orbitin.readline())

def set_orbit_port(port):
    if int(port) < 1:
        raise ValueError("Port number must be a positive integer.")

    orbit = path.join(dir, 'orbit_port')
    with open(orbit, 'w') as out:
        out.write(port)

    return orbit

