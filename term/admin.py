# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from term.models import *
from term.forms import IdentifierForm, IdentifierQualifForm


# class TermInline(admin.TabularInline):
class DescriptionInline(admin.StackedInline):
    model = Description
    extra = 0
    classes = ['collapse']

class TreeNumbersListInline(admin.TabularInline):
    model = TreeNumbersList
    extra = 0
    classes = ['collapse']

class PreviousIndexingListInline(admin.TabularInline):
    model = PreviousIndexingList
    extra = 0
    classes = ['collapse']

class IdentifierForm(admin.ModelAdmin):

	list_display = (
					'descriptor_ui',
					'decs_code',
		)

	form = IdentifierForm

	# Incluindo o formulario de Descriptor
	inlines = [
			DescriptionInline,
			TreeNumbersListInline,
			PreviousIndexingListInline,

	]




# class TermInline(admin.TabularInline):
class DescriptionQualifInline(admin.StackedInline):
    model = DescriptionQualif
    extra = 0
    classes = ['collapse']

class TreeNumbersListQualifInline(admin.TabularInline):
    model = TreeNumbersListQualif
    extra = 0
    classes = ['collapse']

class IdentifierQualifForm(admin.ModelAdmin):

	list_display = (
					'qualifier_ui',
					'decs_code',
					'abbreviation',
		)

	form = IdentifierQualifForm

	# Incluindo o formulario de Descriptor
	inlines = [
			DescriptionQualifInline,
			TreeNumbersListQualifInline,
	]


admin.site.register(Identifier, IdentifierForm)
admin.site.register(IdentifierQualif, IdentifierQualifForm)