# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from tablet.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
