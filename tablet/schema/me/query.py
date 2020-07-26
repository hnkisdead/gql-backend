# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

import graphene


class User(graphene.ObjectType):
    id = graphene.Int(required=True)
    username = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)


class MeQuery(object):
    me = graphene.Field(User)

    @staticmethod
    def resolve_me(parent, info, **kwargs):
        if info.context.user.is_authenticated:
            return info.context.user

        return None
