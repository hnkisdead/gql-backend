# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

import graphene
from graphene_django import DjangoObjectType

from tablet.models import Product as ProductModel


class Product(DjangoObjectType):
    filter_fields = ["name", "category"]

    class Meta:
        model = ProductModel


class ProductsQuery(object):
    products = graphene.List(Product)
    product = graphene.Field(Product, id=graphene.Int(), name=graphene.String(), category=graphene.String())

    def resolve_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_product(self, info, **kwargs):
        id = kwargs.get("id")
        name = kwargs.get("name")

        if id:
            return ProductModel.objects.get(id=id)

        if name:
            return ProductModel.objects.get(name=name)

        return None
