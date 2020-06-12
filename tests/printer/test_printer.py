# -*- coding: utf-8 -*-

import os

from gerritstats.printer.printer import Printer, PrinterException
from gerritstats.proto.proto import Commit


def test_exception():
    exception = PrinterException('exception')
    assert str(exception) == 'exception'


def test_printer():
    config = {
        "gerrit": {
            "host": "https://android.googlesource.com",
            "pass": "",
            "query": {
                "option": ["CURRENT_REVISION"]
            },
            "user": ""
        }
    }

    printer = Printer(config)
    assert printer is not None

    buf = [
        {
            Commit.AUTHOR: 'Jiyong Park <jiyong@google.com>',
            Commit.BRANCH: 'master',
            Commit.COMMIT: '01bca755aed51ea681dbd2cf8237c7173f2cc30a',
            Commit.DATE: '	Mon Jun 08 19:24:09 2020 +0900',
            Commit.DELETIONS: '',
            Commit.INSERTIONS: '',
            Commit.LABELS: '',
            Commit.MESSAGE: 'dex_import that isn\'t available for platform isn\'t installed',
            Commit.REPO: 'platform/build/soong'
        }
    ]

    name = 'output.json'
    printer.run(buf, name)
    assert os.path.isfile(name)
    os.remove(name)

    name = 'output.txt'
    printer.run(buf, name)
    assert os.path.isfile(name)
    os.remove(name)

    name = 'output.xlsx'
    printer.run(buf, name)
    assert os.path.isfile(name)
    os.remove(name)
