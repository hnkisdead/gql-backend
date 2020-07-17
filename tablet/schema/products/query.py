# coding=utf-8
# future
from __future__ import absolute_import, print_function, unicode_literals

import graphene

from tablet.schema.products.resolve_product import resolve_product
from tablet.schema.products.resolve_products import Filter, Product, ProductsPage, Sorter, resolve_products


class ProductsQuery(object):
    products = graphene.Field(
        ProductsPage,
        page=graphene.Int(required=True),
        per_page=graphene.Int(required=True),
        sorters=graphene.List(Sorter, required=False),
        filters=graphene.List(Filter, required=False),
        resolver=resolve_products,
    )
    product = graphene.Field(
        Product, id=graphene.Int(), name=graphene.String(), category=graphene.String(), resolver=resolve_product
    )
