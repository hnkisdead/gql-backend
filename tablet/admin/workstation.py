# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from tablet.models import Workstation


@admin.register(Workstation)
class WorkstationAdmin(admin.ModelAdmin):
    list_display = ["name"]
    filter_horizontal = ["products"]
