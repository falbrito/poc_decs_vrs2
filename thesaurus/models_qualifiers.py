# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

from .models_thesaurus import Thesaurus


LANGUAGE_CODE=(
            ('eng', u'English'),
            ('spa_la', u'Spanish Latin America'),
            ('por', u'Portuguese'),
            ('spa_es', u'Spanish Spain'),
            ('fre', u'French'),
)

YN_OPTION=(
    ('Y','Yes'),('N','No')
)



class IdentifierQualif(models.Model):

    class Meta:
        verbose_name = u'Qualifier'
        verbose_name_plural = u'Qualifiers'
        ordering = ('abbreviation',)

    active = models.BooleanField(u'Enabled', default=True, help_text=u'Check to set it to active')

    thesaurus = models.ForeignKey(Thesaurus, null=True, blank=True, default=None)

    # MESH Qualifier Unique Identifier
    qualifier_ui = models.CharField(u'MESH Qualifier UI', max_length=250, null=True, blank=True)

    # BIREME Qualifier Unique Identifier
    decs_code = models.CharField(u'DeCS Qualifier UI', max_length=250, null=True, blank=True)

    # External Qualifier Unique Identifier
    external_code = models.CharField(u'External Qualifier UI', max_length=250, null=True, blank=True)

    # Abbreviation
    abbreviation = models.CharField(u'Abbreviation', max_length=4, null=True, blank=True)

    # DateCreated
    date_created = models.DateField(u'Date created', null=True, blank=True)

    # DateRevised
    date_revised =  models.DateField(u'Date revised', null=True, blank=True)

    # DateEstablished
    date_established = models.DateField(u'Date established', null=True, blank=True)

    def __str__(self):
        # return '%s' % (self.id)
        return '%s' % (self.abbreviation)



# QualifierRecord
class DescriptionQualif(models.Model):

    class Meta:
        verbose_name = u'Description of Qualifier'
        verbose_name_plural = u'Descriptions of Qualifier'

    identifier = models.ForeignKey(IdentifierQualif, blank=False)

    language_code = models.CharField(u'Language used for description', choices=LANGUAGE_CODE, max_length=10, blank=True)

    # QualifierName
    qualifier_name = models.CharField(u'Qualifier name', max_length=250, blank=False)

    # Annotation
    annotation = models.TextField(u'Annotation', max_length=1500, null=True, blank=True)

    # HistoryNote
    history_note = models.TextField(u'History note', max_length=1500, null=True, blank=True)

    # OnlineNote
    online_note = models.TextField(u'Online note', max_length=1500, null=True, blank=True)

    # ScopeNote (esse campo pertence a ConceptList porém ele esta traduzido)
    scope_note = models.TextField(u'Scope note', max_length=1500, null=True, blank=True)

    def __str__(self):
        # return '%s' % (self.qualifier_name)
        return '%s' % (self.id)




# Tree numbers for qualifiers
class TreeNumbersListQualif(models.Model):

    class Meta:
        verbose_name = u'Tree number for qualifier'
        verbose_name_plural = u'Tree numbers for qualifiers'

    identifier = models.ForeignKey(IdentifierQualif, blank=False)

    # Tree Number
    tree_number = models.CharField(u'Tree number', max_length=250, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.id)




# TermListQualif
class TermListQualif(models.Model):

    class Meta:
        verbose_name = u'Term'
        verbose_name_plural = u'Terms'

    LEXICALTAG_OPTION=(
        ('ABB','ABB - Abbreviation'),
        ('ABX','ABX - Embedded abbreviation'),
        ('ACR','ACR - Acronym'),
        ('ACX','ACX - Embedded acronym'),
        ('EPO','EPO - Eponym'),
        ('LAB','LAB - Lab number'),
        ('NAM','NAM - Proper name'),
        ('NON','NON - None'),
        ('TRD','TRD - Trade name'),
    )

    identifier = models.ForeignKey(IdentifierQualif, blank=False)

    language_code = models.CharField(u'Language used for description', choices=LANGUAGE_CODE, max_length=10, blank=True)

    # ConceptPreferredTermYN
    concept_preferred_term = models.CharField(u'Concept preferred term', choices=YN_OPTION, max_length=1, blank=True)

    # IsPermutedTermYN
    is_permuted_term = models.CharField(u'Is permuted term', choices=YN_OPTION, max_length=1, blank=True)

    # LexicalTag
    lexical_tag =  models.CharField(u'Lexical categories', choices=LEXICALTAG_OPTION, max_length=3, blank=True)

    # RecordPreferredTerm
    record_preferred_term = models.CharField(u'Record preferred term', choices=YN_OPTION, max_length=1, blank=True)

    # TermUI
    term_ui = models.CharField(u'Term unique identifier', max_length=250, null=True, blank=True)

    # String
    term_string = models.CharField(u'String', max_length=250, blank=False)

    # EntryVersion
    entry_version = models.CharField(u'Entry version', max_length=250, blank=True)

    # DateCreated
    date_created = models.DateField(u'Date created', null=True, blank=True)

    def __str__(self):
        return '%s' % (self.id)