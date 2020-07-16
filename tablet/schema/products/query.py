# coding=utf-8
# future
from __future__ import absolute_import, print_function, unicode_literals

import graphene
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator as DjangoPaginator
from graphene import ObjectType
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


class Paginator(ObjectType):
    num_pages = graphene.Int()
    count = graphene.Int()
    per_page = graphene.Int()


class ProductsPage(ObjectType):
    object_list = graphene.List(Product)
    paginator = graphene.Field(Paginator)

    def resolve_object_lists(self, info):
        return self.object_list

    def resolve_paginator(self, info):
        return self.paginator


class ProductsQuery(object):
    products = graphene.Field(
        ProductsPage,
        page=graphene.Int(required=True),
        per_page=graphene.Int(required=True),
        sorters=graphene.List(Sort, required=False),
        filters=graphene.List(Filter, required=False),
    )
    product = Product(id=graphene.Int(), name=graphene.String(), category=graphene.String())

    def resolve_products(self, info, page, per_page, sorters=None, filters=None):
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

    def resolve_product(self, info, **kwargs):
        id = kwargs.get("id")
        name = kwargs.get("name")

        if id:
            return ProductModel.objects.get(id=id)

        if name:
            return ProductModel.objects.get(name=name)

        return None
