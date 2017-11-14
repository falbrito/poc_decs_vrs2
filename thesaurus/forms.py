# -*- coding: utf-8 -*-

from django import forms

from thesaurus.models_thesaurus import Thesaurus

from thesaurus.models_qualifiers import *

from thesaurus.models_descriptors import *


class ThesaurusForm(forms.ModelForm):

	class Meta:
		model = Thesaurus
		# fields = '__all__'
		exclude = ()


class QualifierForm(forms.ModelForm):

    class Meta:
        model = IdentifierQualif
        fields = '__all__'
        # exclude = ()


class DescriptorForm(forms.ModelForm):

    class Meta:
        model = IdentifierDesc
        # fields = '__all__'
        exclude = ()        
