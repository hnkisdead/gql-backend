# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from typing import TYPE_CHECKING

from tablet.models import Product as ProductModel

if TYPE_CHECKING:
    from tablet.schema.products.mutations.create_product import CreateProductPayload


def create_product(payload):
    # type: (CreateProductPayload) -> ProductModel

    if ProductModel.objects.filter(name=payload.name, category=payload.category).exists():
        raise Exception("Продукт с таким название в данной категории уже существует")

    return ProductModel.objects.create(name=payload.name, category=payload.category)
