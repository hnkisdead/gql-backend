# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from tablet.models import Product as ProductModel
from tablet.schema.products.types import Product


def create_product(product):
    # type: (Product) -> ProductModel

    if ProductModel.objects.filter(name=product.name, category=product.category).exists():
        raise Exception("Продукт с таким название в данной категории уже существует")

    return ProductModel.objects.create(name=product.name, category=product.category)
