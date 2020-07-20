# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from typing import TYPE_CHECKING, Text

from django.db.models import Q

if TYPE_CHECKING:
    from tablet.schema.products.resolvers import Sorter, Filter


def sorters_into_order_by_args(sorters):
    # type: ([Sorter]) -> [Text]
    return ["{}{}".format("-" if sorter.order == "desc" else "", sorter.field) for sorter in sorters]


def filters_into_filter_args(filters):
    # type: ([Filter]) -> object
    for filter_item in filters:
        if "id" in filter_item and "exact" in filter_item.id:
            return Q(id__exact=filter_item.id.exact)
        if "name" in filter_item and "contains" in filter_item["name"]:
            return Q(name__contains=filter_item.name.contains)
    return Q()


def empty_resolver(_parent, _info):
    return {}
