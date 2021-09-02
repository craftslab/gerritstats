# -*- coding: utf-8 -*-

import json
import os
import sys

from .cmd.argument import Argument
from .logger.logger import Logger
from .printer.printer import Printer, PrinterException
from .querier.querier import Querier, QuerierException


def load(name):
    with open(name, "r") as f:
        if name.endswith(".json"):
            data = json.load(f)
        else:
            data = None
    return data


def main():
    argument = Argument()
    arg = argument.parse(sys.argv)

    if os.path.exists(arg.config_file) and arg.config_file.endswith(".json"):
        config = load(arg.config_file)
    else:
        Logger.error("config invalid: %s" % arg.config_file)
        return -1

    if len(arg.gerrit_query.strip()) == 0:
        Logger.error("query invalid: %s" % arg.gerrit_query)
        return -2

    query = arg.gerrit_query.strip().split(",")

    if (
        os.path.exists(arg.output_file)
        or os.path.splitext(arg.output_file)[1] not in Printer.format()
    ):
        Logger.error("output invalid: %s" % arg.output_file)
        return -3

    try:
        querier = Querier(config)
        buf = querier.run(query)
    except QuerierException as e:
        Logger.error(str(e))
        return -4

    try:
        printer = Printer(config)
        printer.run(buf, arg.output_file)
    except PrinterException as e:
        Logger.error(str(e))
        return -5

    return 0
