# coding=utf-8
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots["test_empty empty"] = {"products": {"objectList": []}}

snapshots["test_non_empty non empty"] = {
    "products": {"objectList": [{"id": 1, "name": "\u0413\u0430\u0432\u0430\u0439\u0441\u043a\u0430\u044f"}]}
}
