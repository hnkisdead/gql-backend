# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

import graphene

from tablet.schema.products.mutation import ProductsMutationsNamespace
from tablet.schema.products.query import ProductsQuery
from tablet.schema.tablet.query import TabletQuery
from tablet.schema.workstation.query import WorkstationQuery


class Query(ProductsQuery, WorkstationQuery, TabletQuery, graphene.ObjectType):
    pass


class Mutation(ProductsMutationsNamespace, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
