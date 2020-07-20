# coding=utf-8
# future
from __future__ import absolute_import, print_function, unicode_literals

import graphene

from tablet.schema.products.resolvers import Filter, ProductsPage, Sorter, resolve_product, resolve_products
from tablet.schema.products.types import Product


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
        Product,
        product_id=graphene.Int(name="id"),
        name=graphene.String(),
        category=graphene.String(),
        resolver=resolve_product,
    )
