# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

import graphene

from tablet.schema.products.types import Product
from tablet.services.product_services.update_product import update_product


class UpdateProductMutation(graphene.Mutation):
    """
    # Обновляет поля у продукта с указанным ID

    **Поля**
    1. Название
    1. Категория
    """

    class Arguments(object):
        product_id = graphene.Int(required=True, name="id", description="ID продукта")
        name = graphene.String(required=True, description="Название продукта")
        category = graphene.String(required=True, description="Категория продукта")

    product = graphene.Field(Product)

    @staticmethod
    def mutate(_parent, _info, product_id, name, category):
        product = update_product(Product(id=product_id, name=name, category=category))

        return UpdateProductMutation(product=product)
