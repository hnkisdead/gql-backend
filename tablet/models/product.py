# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    category = models.CharField(max_length=255, verbose_name="Категория")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return "{} {}".format(self.name, self.category)
