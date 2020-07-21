# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from typing import Any

import graphene

from tablet.schema.products.types import Product
from tablet.schema.types import ProductAlreadyExistsError, Status
from tablet.services import product_services

CREATE_PRODUCT_DESCRIPTION = """
### Создание продукта

1. Имя 
2. Категория
"""


class CreateProductError(graphene.Union):
    class Meta:
        types = [ProductAlreadyExistsError]


class CreateProductData(graphene.ObjectType):
    recordID = graphene.Int()
    record = graphene.Field(Product)
    status = graphene.Field(Status)
    error = graphene.Field(CreateProductError)


class CreateProductPayload(graphene.InputObjectType):
    name = graphene.String(required=True, description="Имя")
    category = graphene.String(required=True, description="Категория")


def create_product(_parent, _info, payload):
    # type: (Any, Any, CreateProductPayload) -> CreateProductData
    try:
        product = product_services.create_product(payload)
        return CreateProductData(recordID=product.id, record=product)
    except Exception as e:
        return CreateProductData(status=Status.ERROR, error=ProductAlreadyExistsError(e.message))
