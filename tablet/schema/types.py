# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

import graphene
from graphene import ObjectType


class Paginator(ObjectType):
    num_pages = graphene.Int()
    count = graphene.Int()
    per_page = graphene.Int()


class StringFilter(graphene.InputObjectType):
    exact = graphene.String()
    contains = graphene.String()


class IntegerFilter(graphene.InputObjectType):
    exact = graphene.Int()
    gt = graphene.Int()
    gte = graphene.Int()
    lt = graphene.Int()
    lte = graphene.Int()


class SortOrder(graphene.Enum):
    ASC = "asc"
    DESC = "desc"


class Status(graphene.Enum):
    OK = "ok"
    ERROR = "error"


class BaseError(graphene.ObjectType):
    message = graphene.String()


class ProductAlreadyExistsError(BaseError):
    pass


class ProductDoesntExistsError(BaseError):
    pass
