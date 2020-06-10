# -*- coding: utf-8 -*-

import os

from gerritstats.main import load
from gerritstats.gerrit.gerrit import Gerrit, GerritException


def test_exception():
    exception = GerritException('exception')
    assert str(exception) == 'exception'


def test_gerrit():
    config = load(os.path.join(os.path.dirname(__file__), '../../gerritstats/config/config.json'))

    gerrit = Gerrit(config)
    assert gerrit is not None

    buf = gerrit.get(1325676)
    assert buf is not None

    buf = gerrit.query('change:1325676', 0)
    assert buf is not None
