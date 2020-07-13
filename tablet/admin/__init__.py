# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from .product import ProductAdmin
from .tablet import TabletAdmin
from .workstation import WorkstationAdmin

__all__ = [ProductAdmin, WorkstationAdmin, TabletAdmin]
