# -*- coding: utf-8 -*-

from gerritstats.gerrit.gerrit import Gerrit, GerritException


def test_exception():
    exception = GerritException('exception')
    assert str(exception) == 'exception'


def test_gerrit():
    config = {
        "gerrit": {
            "host": "https://android-review.googlesource.com",
            "pass": "",
            "query": {
                "option": ["CURRENT_REVISION"]
            },
            "user": ""
        }
    }

    gerrit = Gerrit(config)
    assert gerrit is not None

    buf = gerrit.get(1325676)
    assert buf is not None

    buf = gerrit.query('change:1325676', 0)
    assert buf is not None
