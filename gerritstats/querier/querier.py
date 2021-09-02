# -*- coding: utf-8 -*-

from ..gerrit.gerrit import Gerrit
from ..proto.proto import Commit


class QuerierException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self._info = info

    def __str__(self):
        return self._info


class Querier(object):
    def __init__(self, config=None):
        if config is None:
            raise QuerierException("config invalid")
        self.gerrit = Gerrit(config)

    def _build(self, data):
        def _labels(data):
            buf = []
            for key, val in data.items():
                if val.get("all", None) is not None:
                    for item in val["all"]:
                        if item.get("value", 0) != 0:
                            buf.append(
                                "%s:%s:%d" % (key, item["username"], item["value"])
                            )
            return ",".join(buf)

        return {
            Commit.BRANCH: data["branch"],
            Commit.COMMIT: data["_number"],
            Commit.DELETIONS: data["deletions"],
            Commit.INSERTIONS: data["insertions"],
            Commit.LABELS: _labels(data["labels"]),
            Commit.MESSAGE: data["subject"].split("\n")[0],
            Commit.OWNER: "%s <%s>"
            % (data["owner"].get("name", ""), data["owner"].get("email", "")),
            Commit.REPO: data["project"],
            Commit.SUBMITTED: data.get("submitted", "").split(".")[0],
            Commit.UPDATED: data.get("updated", "").split(".")[0],
        }

    def _fetch(self, search, start):
        buf = self.gerrit.query(search, start)
        if len(buf) == 0:
            return []
        if buf[-1].get(u"_more_changes", False) is False:
            return buf
        buf.extend(self._fetch(search, start + len(buf)))
        return buf

    def run(self, search):
        commits = []
        buf = self._fetch(search, 0)
        for item in buf:
            commit = self.gerrit.get(item["id"])
            if commit is not None:
                commits.append(self._build(commit))

        return commits
