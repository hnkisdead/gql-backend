# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

import graphene
from graphene_django import DjangoObjectType

from tablet.models import Workstation as WorkstationModel


class Workstation(DjangoObjectType):
    class Meta:
        model = WorkstationModel


class WorkstationQuery(object):
    workstations = graphene.List(Workstation)

    def resolve_workstations(self, info, **kwargs):
        return WorkstationModel.objects.all()
