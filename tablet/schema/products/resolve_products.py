# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from typing import Any

import graphene
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator as DjangoPaginator
from graphene import ObjectType
from graphene_django import DjangoObjectType

from tablet.models import Product as ProductModel
from tablet.schema.helpers import filters_into_filter_args, sorters_into_order_by_args
from tablet.schema.types import IntegerFilter, Paginator, SortOrder, StringFilter


class SortableFields(graphene.Enum):
    ID = "id"
    NAME = "name"
    CATEGORY = "category"


class Sorter(graphene.InputObjectType):
    field = SortableFields()
    order = SortOrder()


class Filter(graphene.InputObjectType):
    id = IntegerFilter()
    name = StringFilter()
    category = StringFilter()

    OR = graphene.List(lambda: Filter)
    AND = graphene.List(lambda: Filter)
    NOT = graphene.Field(lambda: Filter)


class Product(DjangoObjectType):
    class Meta:
        model = ProductModel


class ProductsPage(ObjectType):
    object_list = graphene.List(Product)
    paginator = graphene.Field(Paginator)


def resolve_products(_parent, _info, page, per_page, sorters=None, filters=None):
    # type: (Any, Any, int, int, [Sorter], [Filter]) -> ProductsPage
    if not sorters:
        sorters = []

    if not filters:
        filters = []

    order_by_args = sorters_into_order_by_args(sorters)
    filter_args = filters_into_filter_args(filters)
    queryset = ProductModel.objects.order_by(*order_by_args).filter(filter_args)
    paginator = DjangoPaginator(queryset, per_page)

    try:
        return paginator.page(page)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)
