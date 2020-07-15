# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

import graphene
from graphene_django import DjangoObjectType

from tablet.models import Tablet as TabletModel


class Tablet(DjangoObjectType):
    class Meta:
        model = TabletModel


class TabletQuery(object):
    tablet = graphene.List(Tablet)

    def resolve_tablet(self, info, **kwargs):
        return TabletModel.objects.all()
