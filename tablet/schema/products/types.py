# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

import graphene
from graphene_django import DjangoObjectType

from tablet.models import Product as ProductModel


class Product(DjangoObjectType):
    name = graphene.String()
    category = graphene.String()

    class Meta:
        model = ProductModel
