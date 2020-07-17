# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from tablet.models import Product as ProductModel


def resolve_product(_parent, _info, product_id=None, name=None):
    if product_id:
        return ProductModel.objects.filter(id=product_id).first()

    if name:
        return ProductModel.objects.filter(name=name).first()

    return None
