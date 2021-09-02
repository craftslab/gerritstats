# -*- coding: utf-8 -*-

import argparse

from ..printer.printer import Printer
from .version import VERSION


class Argument(object):
    def __init__(self):
        self._parser = argparse.ArgumentParser()
        self._add()

    def _add(self):
        self._parser.add_argument(
            "-c",
            "--config-file",
            dest="config_file",
            help="config file, format: .json",
            required=True,
        )
        self._parser.add_argument(
            "-o",
            "--output-file",
            dest="output_file",
            help="output file, format: " + ", ".join(Printer.format()),
            required=True,
        )
        self._parser.add_argument(
            "-q",
            "--gerrit-query",
            dest="gerrit_query",
            help="gerrit query, format: QUERY1,QUERY2,...",
            required=True,
        )
        self._parser.add_argument("-v", "--version", action="version", version=VERSION)

    def parse(self, argv):
        return self._parser.parse_args(argv[1:])
