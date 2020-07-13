# coding=utf-8
from __future__ import absolute_import, print_function, unicode_literals

from graphene_django.types import DjangoObjectType

from .models import Tablet, Workstation


class TabletType(DjangoObjectType):
    class Meta:
        model = Tablet
        description = "Планшет"
