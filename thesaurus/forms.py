# -*- coding: utf-8 -*-

from django import forms

from thesaurus.models import Thesaurus

class ThesaurusForm(forms.ModelForm):

	class Meta:
		model = Thesaurus
		# fields = '__all__'
		exclude = ()