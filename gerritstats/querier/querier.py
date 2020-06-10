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
            raise QuerierException('config invalid')
        self.gerrit = Gerrit(config)

    def _build(self, data):
        def _labels(data):
            buf = []
            for key, val in data.items():
                if val.get('all', None) is not None:
                    approval = val['all'][-1].get('value', 0)
                else:
                    approval = 0
                buf.append('%s:%d' % (key, approval))
            return ','.join(buf)

        return {
            Commit.AUTHOR: '%s <%s>' % (data['owner'].get('name', ''), data['owner'].get('email', '')),
            Commit.BRANCH: data['branch'],
            Commit.COMMIT: data['_number'],
            Commit.DATE: data['updated'].split('.')[0],
            Commit.DELETIONS: data['deletions'],
            Commit.INSERTIONS: data['insertions'],
            Commit.LABELS: _labels(data['labels']),
            Commit.MESSAGE: data['subject'].split('\n')[0],
            Commit.REPO: data['project']
        }

    def _fetch(self, search, start):
        buf = self.gerrit.query(search, start)
        if len(buf) == 0:
            return []
        if buf[-1].get(u'_more_changes', False) is False:
            return buf
        buf.extend(self._fetch(search, start + len(buf)))
        return buf

    def run(self, search):
        commits = []
        buf = self._fetch(search, 0)
        for item in buf:
            commit = self.gerrit.get(item['id'])
            if commit is not None:
                commits.append(self._build(commit))

        return commits
