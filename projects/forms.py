from django import forms
from .models import *

class PrincipiForm(forms.Form):
    principi = forms.CharField(max_length=100)

class ObjectiuForm(forms.Form):
	objectiu = forms.CharField(max_length=100)
	descripcio = forms.CharField(widget=forms.Textarea)
	principis = forms.ModelChoiceField(queryset=Principi.objects.all(), empty_label=None)

class ProjecteForm(forms.Form):
	asd = "asd"