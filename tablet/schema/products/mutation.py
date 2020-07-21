# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

import graphene

from tablet.schema.helpers import empty_resolver

from .mutations.create_product import (
    CREATE_PRODUCT_DESCRIPTION,
    CreateProductData,
    CreateProductPayload,
    create_product,
)
from .mutations.update_product import (
    UPDATE_PRODUCT_DESCRIPTION,
    UpdateProductData,
    UpdateProductPayload,
    update_product,
)


class ProductsMutations(graphene.ObjectType):
    create = graphene.Field(
        CreateProductData,
        payload=graphene.Argument(CreateProductPayload, required=True),
        description=CREATE_PRODUCT_DESCRIPTION,
        resolver=create_product,
    )
    update = graphene.Field(
        UpdateProductData,
        payload=graphene.Argument(UpdateProductPayload, required=True),
        description=UPDATE_PRODUCT_DESCRIPTION,
        resolver=update_product,
    )


class ProductsMutationsNamespace(object):
    products = graphene.Field(ProductsMutations, resolver=empty_resolver)
