# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from tablet.models import Product as ProductModel


def resolve_product(_parent, _info, **kwargs):
    id = kwargs.get("id")
    name = kwargs.get("name")

    if id:
        return ProductModel.objects.get(id=id)

    if name:
        return ProductModel.objects.get(name=name)

    return None
