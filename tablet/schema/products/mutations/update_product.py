# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from typing import Any

import graphene

from tablet.schema.products.types import Product
from tablet.schema.types import ProductDoesntExistsError, Status
from tablet.services import product_services


class UpdateProductError(graphene.Union):
    class Meta:
        types = [ProductDoesntExistsError]


class UpdateProductData(graphene.ObjectType):
    recordID = graphene.Int()
    record = graphene.Field(Product)
    status = graphene.Field(Status)
    error = graphene.Field(UpdateProductError)


class UpdateProductPayload(graphene.InputObjectType):
    id = graphene.Int(required=True, description="ID")
    name = graphene.String(required=True, description="Имя")
    category = graphene.String(required=True, description="Категория")


def update_product(_parent, _info, payload):
    # type: (Any, Any, UpdateProductPayload) -> UpdateProductData
    try:
        product = product_services.update_product(payload)
        return UpdateProductData(recordID=product.id, record=product)
    except Exception as e:
        return UpdateProductData(status=Status.ERROR, error=ProductDoesntExistsError(e.message))
