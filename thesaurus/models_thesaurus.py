# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# thesaurus fields
class Thesaurus(models.Model):

    class Meta:
            verbose_name = u'Thesaurus'
            verbose_name_plural = u'Thesaurus'

    thesaurus_name = models.CharField(u'Thesaurus name', max_length=250, blank=False)

    thesaurus_author = models.CharField(u'Author', max_length=250, blank=False)

    thesaurus_scope = models.CharField(u'Scope', max_length=250, blank=False)


    def __str__(self):
        return '%s' % (self.thesaurus_name)