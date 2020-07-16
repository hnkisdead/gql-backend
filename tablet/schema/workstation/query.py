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

    @staticmethod
    def resolve_workstations(parent, info, **kwargs):
        return WorkstationModel.objects.all()
