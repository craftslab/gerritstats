# -*- coding: utf-8 -*-

import pprint
import requests

from gerritstats.querier.querier import Querier, QuerierException


def test_exception():
    exception = QuerierException("exception")
    assert str(exception) == "exception"


def test_querier():
    config = {
        "gerrit": {
            "host": "https://android-review.googlesource.com",
            "pass": "",
            "query": {"option": ["CURRENT_REVISION"]},
            "user": "",
        }
    }

    querier = Querier(config)
    assert querier is not None

    buf = {
        "project": "platform/build/soong",
        "branch": "master",
        "subject": "dex_import that isn't available for platform isn't installed",
        "updated": "Mon Jun 08 19:24:09 2020 +0900",
        "insertions": 4,
        "deletions": 2,
        "_number": 1325676,
        "owner": {
            "name": "Jiyong Park",
            "email": "jiyong@google.com",
        },
        "labels": {
            "Code-Review": {
                "all": [
                    {
                        "value": 0,
                        "_account_id": 1000000,
                        "name": "Jiyong Park",
                        "username": "jiyong",
                    },
                    {
                        "value": 2,
                        "date": "2020-06-08 19:24:09.000000000",
                        "permitted_voting_range": {"min": 2, "max": 2},
                        "_account_id": 1000000,
                        "name": "Jiyong Park",
                        "email": "jiyong@google.com",
                        "username": "jiyong",
                    },
                ],
            },
        },
    }

    buf = querier._build(buf)
    assert buf is not None

    try:
        buf = querier._fetch("change:1325676", 0)
    except requests.exceptions.InvalidSchema:
        buf = None

    if buf is not None:
        pprint.pprint(buf)
