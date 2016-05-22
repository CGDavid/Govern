from django import forms
from .models import *

class PrincipiForm(forms.Form):
    principi = forms.CharField(max_length=100)

class ObjectiuForm(forms.Form):
	objectiu = forms.CharField(max_length=100)
	descripcio = forms.CharField(widget=forms.Textarea)
	#principis = forms.ModelChoiceField(queryset=Principi.objects.all(), empty_label=None)

class ProjecteForm(forms.Form):
	asd = "asd"

class MetricaForm(forms.Form):
	metrica = forms.CharField(max_length=100)
	descripcio = forms.CharField(widget=forms.Textarea)
	unitat = forms.CharField(max_length=100)
	vMin = forms.IntegerField()
	vMax = forms.IntegerField()
	objectiu = forms.ModelChoiceField(queryset=Objectiu.objects.exclude(), empty_label=None)
