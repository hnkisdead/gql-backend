# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

import graphene

from tablet.schema.helpers import empty_resolver
from tablet.schema.products.create_product import CreateProductMutation
from tablet.schema.products.update_product import UpdateProductMutation


class ProductsMutations(graphene.ObjectType):
    create = CreateProductMutation.Field()
    update = UpdateProductMutation.Field()


class ProductsMutationsNamespace(object):
    products = graphene.Field(ProductsMutations, resolver=empty_resolver)
