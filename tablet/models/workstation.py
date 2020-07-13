# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible

from tablet.models.product import Product


@python_2_unicode_compatible
class Workstation(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, related_name="workstations")

    class Meta:
        verbose_name = "Станция"
        verbose_name_plural = "Станции"

    def __str__(self):
        return self.name
