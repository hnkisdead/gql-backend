# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

import graphene

from tablet.schema.products.types import Product
from tablet.services.product_services.create_product import create_product


class CreateProductMutation(graphene.Mutation):
    class Arguments(object):
        name = graphene.String(required=True)
        category = graphene.String(required=True)

    product = graphene.Field(Product)

    def mutate(root, info, name, category):
        product = create_product(Product(name=name, category=category))

        return CreateProductMutation(product=product)
