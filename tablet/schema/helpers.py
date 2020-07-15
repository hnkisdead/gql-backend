# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from django.db.models import Q


def sorters_into_order_by_args(sorters):
    return ["{}{}".format("-" if sorter["order"] == "desc" else "", sorter["field"]) for sorter in sorters]


def filters_into_filter_args(filters):
    for filter_item in filters:
        if "id" in filter_item and "exact" in filter_item["id"]:
            return Q(id__exact=filter_item["id"]["exact"])
        if "name" in filter_item and "exact" in filter_item["name"]:
            return Q(name__exact=filter_item["name"]["exact"])
    return Q()
