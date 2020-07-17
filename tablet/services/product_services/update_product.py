# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from tablet.models import Product as ProductModel
from tablet.schema.products.types import Product


def update_product(product):
    # type: (Product) -> ProductModel
    return ProductModel.objects.filter(id=product.id).update(name=product.name, category=product.category)
