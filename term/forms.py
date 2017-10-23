# -*- coding: utf-8 -*-

from django import forms

from term.models import Identifier, IdentifierQualif

class IdentifierForm(forms.ModelForm):

    class Meta:
        model = Identifier
        fields = '__all__'
        # exclude = ()


class IdentifierQualifForm(forms.ModelForm):

    class Meta:
        model = IdentifierQualif
        # fields = '__all__'
        exclude = ()        
