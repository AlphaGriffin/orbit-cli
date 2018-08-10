#!/usr/bin/env python3
#
# Copyright (C) 2018 Alpha Griffin
# @%@~LICENSE~@%@

from ag.orbit.command import main
from ag.orbit.ops.advertisement import Advertise
from ag.orbit.cli import arg
from ag.orbit.cli.network import broadcast


def run(args):
    args = args if args else None

    print()
    print("Advertise token crowd-sale/faucet...")

    if args:
        if len(args) < 7 or len(args) > 8:
            print()
            raise ValueError("Expecting no less than 7 and no more than 8 arguments")

    exchange_rate = arg(args, 0, "Exchange rate",
            description="Price in satoshi for a single indivisible token unit.", hints=[
                "A negative number indicates fractional value (e.g. -5 = 1/5 i.e. 5 units per satoshi).",
                "The text \"NONE\" indicates free exchange (faucet)."],
            none="NONE")
    if exchange_rate:
        exchange_rate = int(exchange_rate)

    units_avail = arg(args, 1, "Available units",
            description="The number of indivisible token units to make available.", hints=[
                "Use \"ALL\" to dedicate the entire available supply.",
                #"Use \"ANY\" to make the entire supply available without dedicating them.",
                #"Note that unless \"ANY\" is used, units are set aside made unavailable for any other use."],
                "Note that the units are set aside for this purpose and made unavailable for any other use."],
            none="ALL")
    if units_avail:
        units_avail = int(units_avail)

    units_min = arg(args, 2, "Minimum units",
            description="The minimum number of units each user is required to receive.", hints=[
                "Use \"NONE\" to have no per-user minimum."],
            none="NONE")
    if units_min:
        units_min = int(units_min)

    units_max = arg(args, 3, "Maximum units",
            description="The maximum number of units each user is allowed to receive.", hints=[
                "Use \"NONE\" to have no per-user maximum."],
            none="NONE")
    if units_max:
        units_max = int(units_max)

    block_begin = arg(args, 4, "Beginning block",
            description="The block number (height) at which the crowd-sale or faucet begins.", hints=[
                "Any payments sent before the beginning block will be ignored.",
                "Use \"NOW\" to begin in the block immediately following the confirmation of this transaction."],
            none="NOW")
    if block_begin:
        block_begin = int(block_begin)

    block_end = arg(args, 5, "Ending block",
            description="The block number (height) at which the crowd-sale or faucet will terminate.", hints=[
                "Use \"FOREVER\" to remain active until supply runs out."],
            none="FOREVER")
    if block_end:
        block_end = int(block_end)

    block_deliver = arg(args, 6, "Delivery block",
            description="The block number (height) at which tokens are first delivered to the users.", hints=[
                "Use \"ANY\" for immediate delivery."],
            none="ANY")
    if block_deliver:
        block_deliver = int(block_deliver)

    if exchange_rate and block_begin:
        preregister = arg(args, 7, "Preregister",
                description="If true, indicates that users are allowed to register before the beginning block.", hints=[
                    "Crowd-sale payments are still only accepted no sooner than the beginning block.",
                    "Any payments sent along with an early registration will be ignored.",
                    "Leave blank to not allow preregistration (the default). Otherwise, use \"TRUE\", \"YES\", or \"Y\""],
                optional=True)
        if preregister:
            if preregister == "TRUE" or preregister == "YES" or preregister == "Y":
                preregister = True
            else:
                raise ValueError("Preregister flag, if used, must be \"TRUE\", \"YES\", or \"Y\"")
    elif args and len(args) > 7:
        raise ValueError("Preregister flag may only be used when exchange rate and beginning block are used")
    else:
        preregister = False

    advertise(exchange_rate, units_avail, units_min, units_max, block_begin, block_end, block_deliver, preregister)

def advertise(exchange_rate, units_avail, units_min, units_max, block_begin, block_end, block_deliver, preregister=False):
    op = Advertise(exchange_rate, units_avail, units_min, units_max, block_begin, block_end, block_deliver, preregister)
    broadcast(op)


if __name__ == '__main__':
    main(run)

