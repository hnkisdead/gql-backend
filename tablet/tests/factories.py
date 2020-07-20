# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

import factory

from tablet.models import Product


class ProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = Product
