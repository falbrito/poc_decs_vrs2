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



# For Qualifier ---------------------------------------------------
class IdentifierQualif(models.Model):

    class Meta:
        verbose_name = u'Qualifier'
        verbose_name_plural = u'Qualifiers'

    thesaurus = models.ForeignKey(Thesaurus, null=True, blank=True, default=None)

    # QualifierUI
    qualifier_ui = models.CharField( u'MESH code for Qualifier', max_length=250, null=True, blank=True)

    # BIREME DeCS Code 
    decs_code = models.CharField( u'DeCS code', max_length=250, null=True, blank=True)

    # Abbreviation
    abbreviation = models.CharField( u'Abbreviation', max_length=4, null=True, blank=True)

    # DateCreated
    date_created = models.DateField( u'Date created', null=True, blank=True )       

    # DateRevised
    date_revised =  models.DateField( u'Date revised', null=True, blank=True )

    # DateEstablished
    date_established = models.DateField( u'Date established', null=True, blank=True )


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

    language_code = models.CharField( 
        u'Language used for description', 
        choices=LANGUAGE_CODE, 
        max_length=10, 
        blank=True,
    )

    # QualifierName
    qualifier_name = models.CharField( u'Qualifier name', max_length=250, blank=False )

    # Annotation
    annotation = models.TextField( u'Annotation', max_length=1500, null=True, blank=True )

    # HistoryNote
    history_note = models.TextField( u'History note', max_length=1500, null=True, blank=True )

    # OnlineNote
    online_note = models.TextField( u'Online note', max_length=1500, null=True, blank=True )

    identifier_qualif = models.ForeignKey(IdentifierQualif, blank=False)

    def __str__(self):
        return '%s' % (self.qualifier_name)




# Tree numbers for qualifiers
class TreeNumbersListQualif(models.Model):

    # Tree Number
    tree_number = models.CharField( u'Tree number', max_length=250, null=True, blank=True )
    identifier = models.ForeignKey(IdentifierQualif, blank=False)    

    class Meta:
        verbose_name = u'Tree number for qualifier'
        verbose_name_plural = u'Tree numbers for qualifiers'

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
    descriptor_class = models.CharField(
        u'Descriptor class',
        choices=DESCRIPTOR_CLASS_CODE,
        max_length=2,
        blank=True,
    )

    # DescriptorUI
    descriptor_ui = models.CharField( u'MESH code', max_length=250, null=True, blank=True)

    # BIREME DeCS Code 
    decs_code = models.CharField( u'DeCS code', max_length=250, null=True, blank=True)

    # NLMClassificationNumber
    nlm_class_number = models.CharField( u'NLM classification number', max_length=250, null=True, blank=True )

    # DateCreated
    date_created = models.DateField( u'Date created', null=True, blank=True )       

    # DateRevised
    date_revised =  models.DateField( u'Date revised', null=True, blank=True )

    # DateEstablished
    date_established = models.DateField( u'Date established', null=True, blank=True )

    abbreviation = models.ManyToManyField(IdentifierQualif, verbose_name='Abbreviation', blank=False)


    def __str__(self):
        return '%s' % (self.id)




# Description
class Description(models.Model):

    class Meta:
        verbose_name = u'Description'
        verbose_name_plural = u'Descriptions'


    language_code = models.CharField( 
    	u'Language used for description', 
    	choices=LANGUAGE_CODE, 
    	max_length=10, 
    	blank=True,
    )

    # DescriptorName
    descriptor_name = models.CharField( u'Term name', max_length=250, blank=False )

    # Annotation
    annotation = models.TextField( u'Annotation', max_length=1500, null=True, blank=True )

    # HistoryNote
    history_note = models.TextField( u'History note', max_length=1500, null=True, blank=True )

    # OnlineNote
    online_note = models.TextField( u'Online note', max_length=1500, null=True, blank=True )

    # PublicMeSHNote
    public_mesh_note = models.TextField( u'Public MeSH note', max_length=1500, null=True, blank=True )

    # ConsiderAlso
    consider_also = models.CharField( u'Consider also', max_length=250, null=True, blank=True )

    identifier = models.ForeignKey(Identifier, blank=False)

    def __str__(self):
        # return '%s' % (self.id)
        return '%s' % (self.descriptor_name)




# Tree numbers for descriptors
class TreeNumbersList(models.Model):

    # Tree Number
    tree_number = models.CharField( u'Tree number', max_length=250, null=True, blank=True )
    identifier = models.ForeignKey(Identifier, blank=False)

    class Meta:
        verbose_name = u'Tree number for descriptor'
        verbose_name_plural = u'Tree numbers for descriptors'

    def __str__(self):
        return '%s' % (self.id)




# Previous Indexing List
class PreviousIndexingList(models.Model):

    # PreviousIndexing
    previous_indexing = models.CharField( u'Previous indexing', max_length=250, null=True, blank=True )
    identifier = models.ForeignKey(Identifier, blank=False)

    class Meta:
        verbose_name = u'Previous Indexing'
        verbose_name_plural = u'Previous Indexing'

    def __str__(self):
        return '%s' % (self.id)






