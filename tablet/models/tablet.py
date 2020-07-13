# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible

from tablet.models.workstation import Workstation


@python_2_unicode_compatible
class Tablet(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя", help_text="Имя")
    workstations = models.ManyToManyField(
        Workstation, related_name="tablets", verbose_name="Станции", help_text="Станции"
    )

    class Meta:
        verbose_name = "Планшет"
        verbose_name_plural = "Планшеты"

    def __str__(self):
        return self.name
