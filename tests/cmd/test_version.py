# -*- coding: utf-8 -*-

from gerritstats.cmd.version import VERSION


def test_version():
    assert VERSION is not None and len(VERSION) != 0
