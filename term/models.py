# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

from thesaurus.models import Thesaurus


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



# For Qualifier ---------------------------------------------------
class IdentifierQualif(models.Model):

    class Meta:
        verbose_name = u'Qualifier'
        verbose_name_plural = u'Qualifiers'

    thesaurus = models.ForeignKey(Thesaurus, null=True, blank=True, default=None)

    # QualifierUI
    qualifier_ui = models.CharField(u'MESH code for Qualifier', max_length=250, null=True, blank=True)

    # BIREME DeCS Code 
    decs_code = models.CharField(u'DeCS code', max_length=250, null=True, blank=True)

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

    class Meta:
        ordering = ('abbreviation',)




# QualifierRecord
class DescriptionQualif(models.Model):

    class Meta:
        verbose_name = u'Description of Qualifier'
        verbose_name_plural = u'Descriptions of Qualifier'

    identifier_qualif = models.ForeignKey(IdentifierQualif, blank=False)

    language_code = models.CharField(u'Language used for description', choices=LANGUAGE_CODE, max_length=10, blank=True)

    # QualifierName
    qualifier_name = models.CharField(u'Qualifier name', max_length=250, blank=False)

    # Annotation
    annotation = models.TextField(u'Annotation', max_length=1500, null=True, blank=True)

    # HistoryNote
    history_note = models.TextField(u'History note', max_length=1500, null=True, blank=True)

    # OnlineNote
    online_note = models.TextField(u'Online note', max_length=1500, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.qualifier_name)




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

# For Qualifier ---------------------------------------------------




# thesaurus fields
class Identifier(models.Model):

    class Meta:
        verbose_name = u'Register'
        verbose_name_plural = u'Registers'

    DESCRIPTOR_CLASS_CODE=(
                ('1', u'1 - Topical Descriptor'),
                ('2', u'2 - Publication Types, for example Review'),
                ('3', u'3 - Check Tag, e.g., Male - no tree number'),
                ('4', u'4 - Geographic Descriptor'),
    )

    thesaurus = models.ForeignKey(Thesaurus, null=True, blank=True, default=None)

    # DescriptorClass
    descriptor_class = models.CharField(u'Descriptor class', choices=DESCRIPTOR_CLASS_CODE, max_length=2, blank=True)

    # DescriptorUI
    descriptor_ui = models.CharField(u'MESH code', max_length=250, null=True, blank=True)

    # BIREME DeCS Code 
    decs_code = models.CharField(u'DeCS code', max_length=250, null=True, blank=True)

    # NLMClassificationNumber
    nlm_class_number = models.CharField(u'NLM classification number', max_length=250, null=True, blank=True)

    # DateCreated
    date_created = models.DateField(u'Date created', null=True, blank=True)

    # DateRevised
    date_revised =  models.DateField(u'Date revised', null=True, blank=True)

    # DateEstablished
    date_established = models.DateField(u'Date established', null=True, blank=True)

    abbreviation = models.ManyToManyField(IdentifierQualif, verbose_name='Abbreviation', blank=False)

    def __str__(self):
        return '%s' % (self.id)




# Description
class Description(models.Model):

    class Meta:
        verbose_name = u'Description'
        verbose_name_plural = u'Descriptions'

    identifier = models.ForeignKey(Identifier, blank=False)

    language_code = models.CharField(u'Language used for description', choices=LANGUAGE_CODE, max_length=10, blank=True)

    # DescriptorName
    descriptor_name = models.CharField(u'Term name', max_length=250, blank=False)

    # Annotation
    annotation = models.TextField(u'Annotation', max_length=1500, null=True, blank=True)

    # HistoryNote
    history_note = models.TextField(u'History note', max_length=1500, null=True, blank=True)

    # OnlineNote
    online_note = models.TextField(u'Online note', max_length=1500, null=True, blank=True)

    # ScopeNote (esse campo pertence a ConceptList porém ele esta traduzido)
    scope_note = models.TextField(u'Scope note', max_length=1500, null=True, blank=True)

    # PublicMeSHNote
    public_mesh_note = models.TextField(u'Public MeSH note', max_length=1500, null=True, blank=True)

    # ConsiderAlso
    consider_also = models.CharField(u'Consider also', max_length=250, null=True, blank=True)

    def __str__(self):
        # return '%s' % (self.id)
        return '%s' % (self.descriptor_name)




# Tree numbers for descriptors
class TreeNumbersList(models.Model):

    class Meta:
        verbose_name = u'Tree number for descriptor'
        verbose_name_plural = u'Tree numbers for descriptors'

    identifier = models.ForeignKey(Identifier, blank=False)

    # Tree Number
    tree_number = models.CharField(u'Tree number', max_length=250, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.id)




# Previous Indexing List
class PreviousIndexingList(models.Model):

    class Meta:
        verbose_name = u'Previous Indexing'
        verbose_name_plural = u'Previous Indexing'

    identifier = models.ForeignKey(Identifier, blank=False)

    # PreviousIndexing
    previous_indexing = models.CharField(u'Previous indexing', max_length=250, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.id)




# ConceptList
class ConceptList(models.Model):

    class Meta:
        verbose_name = u'Concept'
        verbose_name_plural = u'Concepts'

    RELATION_NAME_OPTION=(
        ('BRD','BRD - Broader'),
        ('NRW','NRW - Narrower'),
        ('REL','REL - Related but not broader or narrower'),
    )


    identifier = models.ForeignKey(Identifier, blank=False)

    language_code = models.CharField(u'Language used for description', choices=LANGUAGE_CODE, max_length=10, blank=True)

    # PreferredConcept
    preferred_concept = models.CharField(u'Preferred concept', choices=YN_OPTION, max_length=1, blank=True)

    # ConceptUI
    concept_ui = models.CharField(u'Concept unique Identifier', max_length=50, null=True, blank=True)

    # ConceptName
    concept_name = models.CharField(u'Concept name', max_length=250, null=True, blank=True)

    # CASN1Name
    casn1_name = models.TextField(u'Chemical abstract', max_length=1000, null=True, blank=True)

    # RegistryNumber
    registry_number = models.CharField(u'Registry number from CAS', max_length=250, null=True, blank=True)

    # ConceptRelation RelationName
    relation_name = models.CharField(u'Concept relation', choices=RELATION_NAME_OPTION, max_length=3, blank=True)

    # Concept1UI
    concept1_ui = models.CharField(u'First concept in then Concept relation', max_length=250, null=True, blank=True)

    # Concept2UI
    concept2_ui = models.CharField(u'Second concept in then Concept relation', max_length=250, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.id)




# TermList
class TermList(models.Model):

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

    identifier = models.ForeignKey(Identifier, blank=False)

    language_code = models.CharField(u'Language used for description', choices=LANGUAGE_CODE, max_length=10, blank=True)

    # ConceptPreferredTermYN
    concept_preferred_term = models.CharField(u'Concept preferred term', choices=YN_OPTION, max_length=1, blank=True)

    # IsPermutedTermYN
    is_permuted_term = models.CharField(u'Is permuted term', choices=YN_OPTION, max_length=1, blank=True)

    # LexicalTag
    lexical_tag =  models.CharField(u'Is permuted term', choices=LEXICALTAG_OPTION, max_length=3, blank=True)

    # RecordPreferredTerm
    record_preferred_term = models.CharField(u'Record preferred term', choices=YN_OPTION, max_length=1, blank=True)

    # TermUI
    term_ui = models.CharField(u'Term unique identifier', max_length=250, null=True, blank=True)

    # String
    term_string = models.CharField(u'String', max_length=250, blank=False)

    # DateCreated
    date_created = models.DateField(u'Date created', null=True, blank=True)

    def __str__(self):
        return '%s' % (self.id)
