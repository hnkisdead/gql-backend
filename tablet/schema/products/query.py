# coding=utf-8
# future
from __future__ import absolute_import, print_function, unicode_literals

import graphene
from graphene_django import DjangoObjectType

from tablet.models import Product as ProductModel
from tablet.schema.helpers import filters_into_filter_args, sorters_into_order_by_args


class SortableFields(graphene.Enum):
    ID = "id"
    NAME = "name"
    CATEGORY = "category"


class SortOrder(graphene.Enum):
    ASC = "asc"
    DESC = "desc"


class Sort(graphene.InputObjectType):
    field = SortableFields()
    order = SortOrder()


class StringFilter(graphene.InputObjectType):
    exact = graphene.String()
    contains = graphene.String()


class IntegerFilter(graphene.InputObjectType):
    exact = graphene.Int()
    gt = graphene.Int()
    gte = graphene.Int()
    lt = graphene.Int()
    lte = graphene.Int()


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


class ProductsQuery(object):
    products = graphene.List(
        Product, sorters=graphene.List(Sort, required=False), filters=graphene.List(Filter, required=False)
    )
    product = graphene.Field(Product, id=graphene.Int(), name=graphene.String(), category=graphene.String())

    def resolve_products(self, info, sorters=None, filters=None):
        if not sorters:
            sorters = []

        if not filters:
            filters = []

        order_by_args = sorters_into_order_by_args(sorters)
        filter_args = filters_into_filter_args(filters)
        return ProductModel.objects.order_by(*order_by_args).filter(filter_args)

    def resolve_product(self, info, **kwargs):
        id = kwargs.get("id")
        name = kwargs.get("name")

        if id:
            return ProductModel.objects.get(id=id)

        if name:
            return ProductModel.objects.get(name=name)

        return None
