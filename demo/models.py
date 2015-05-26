from django.db import models
from django.utils.translation import ugettext as _


class Person(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')
