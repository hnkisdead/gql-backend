# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from typing import TYPE_CHECKING

from tablet.models import Product as ProductModel

if TYPE_CHECKING:
    from tablet.schema.products.mutations.update_product import UpdateProductPayload


def update_product(payload):
    # type: (UpdateProductPayload) -> ProductModel
    product = ProductModel.objects.filter(id=payload.id).first()

    if not product:
        raise Exception("Продукта не существует")

    product.name = payload.name
    product.category = payload.category
    product.save()
    return product
