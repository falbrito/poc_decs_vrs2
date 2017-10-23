# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from thesaurus.models import Thesaurus

from thesaurus.forms import ThesaurusForm

class ThesaurusForm(admin.ModelAdmin):

	list_display = (
						'thesaurus_name',
					)

	form = ThesaurusForm

admin.site.register(Thesaurus, ThesaurusForm)