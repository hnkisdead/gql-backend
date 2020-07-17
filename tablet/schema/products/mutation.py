# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

import graphene

from tablet.schema.helpers import empty_resolver
from tablet.schema.products.create_product import CreateProductMutation


class ProductsMutation(graphene.ObjectType):
    create = CreateProductMutation.Field()


class Products(object):
    products = graphene.Field(ProductsMutation, resolver=empty_resolver)
