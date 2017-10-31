# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from term.models import *
from term.forms import IdentifierForm, IdentifierQualifForm



# Formulario para Descricao do termo
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

class ConceptListInline(admin.StackedInline):
    model = ConceptList
    extra = 0
    classes = ['collapse']

class TermListInline(admin.StackedInline):
    model = TermList
    extra = 0
    classes = ['collapse']


class IdentifierForm(admin.ModelAdmin):
	list_display = (
					'descriptor_ui',
					'decs_code',
		)

	list_per_page = 15
	filter_horizontal = ('abbreviation',)
	search_fields = ['descriptor_ui','decs_code']

	form = IdentifierForm

	# Incluindo o formulario de Descriptor
	inlines = [
			DescriptionInline,
			TreeNumbersListInline,
			PreviousIndexingListInline,
			ConceptListInline,
			TermListInline,

	]



# Formulario para Descricao do qualificador
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
					'abbreviation',
					'qualifier_ui',
					'decs_code',
		)
	list_per_page = 15
	search_fields = ['qualifier_ui','decs_code','abbreviation']

	form = IdentifierQualifForm

	# Incluindo o formulario de Descriptor
	inlines = [
			DescriptionQualifInline,
			TreeNumbersListQualifInline,
	]



admin.site.register(Identifier, IdentifierForm)
admin.site.register(IdentifierQualif, IdentifierQualifForm)
