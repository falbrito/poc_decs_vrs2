# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from thesaurus.models_thesaurus import Thesaurus
from thesaurus.models_qualifiers import *
from thesaurus.models_descriptors import *

from thesaurus.forms import ThesaurusForm, QualifierForm, DescriptorForm


class ThesaurusForm(admin.ModelAdmin):

	list_display = (
						'thesaurus_name',
					)

	form = ThesaurusForm




# Formulario para Descricao do qualificador
class DescriptionQualifInline(admin.StackedInline):
    model = DescriptionQualif
    extra = 0
    classes = ['collapse']

class TreeNumbersListQualifInline(admin.TabularInline):
    model = TreeNumbersListQualif
    extra = 0
    classes = ['collapse']

class TermListQualifInline(admin.StackedInline):
    model = TermListQualif
    extra = 0
    classes = ['collapse']


class QualifierForm(admin.ModelAdmin):
	list_display = (
					'abbreviation',
					'qualifier_ui',
					'decs_code',
		)
	list_per_page = 15
	search_fields = ['qualifier_ui','decs_code','abbreviation']

	form = QualifierForm

	# Incluindo o formulario de Descriptor
	inlines = [
			DescriptionQualifInline,
			TreeNumbersListQualifInline,
			TermListQualifInline,
	]




# Formulario para Descricao do termo
class DescriptionDescInline(admin.StackedInline):
    model = DescriptionDesc
    extra = 0
    classes = ['collapse']

class TreeNumbersListDescInline(admin.TabularInline):
    model = TreeNumbersListDesc
    extra = 0
    classes = ['collapse']

class PreviousIndexingListDescInline(admin.TabularInline):
    model = PreviousIndexingListDesc
    extra = 0
    classes = ['collapse']

class ConceptListDescInline(admin.StackedInline):
    model = ConceptListDesc
    extra = 0
    classes = ['collapse']

class TermListDescInline(admin.StackedInline):
    model = TermListDesc
    extra = 0
    classes = ['collapse']

class DescriptorForm(admin.ModelAdmin):
	list_display = (
					'descriptor_ui',
					'decs_code',
		)

	list_per_page = 15
	filter_horizontal = ('abbreviation',)
	search_fields = ['descriptor_ui','decs_code']

	form = DescriptorForm

	# Incluindo o formulario de Descriptor
	inlines = [
			DescriptionDescInline,
			TreeNumbersListDescInline,
			PreviousIndexingListDescInline,
			ConceptListDescInline,
			TermListDescInline,

	]




admin.site.register(Thesaurus, ThesaurusForm)
admin.site.register(IdentifierQualif, QualifierForm)
admin.site.register(IdentifierDesc, DescriptorForm)
