from django import forms
from .models import *
from functools import partial

ESTAT = (
    ('PE','Pendent'),
    ('PR','Progres'),
    ('RE','Rebutjat'),
    ('FI','Finalitzat'),
)

TIPUS = (
    ('F2P','Free To Play'),
    ('CO','Convencional'),
    ('ALT','Altres'),
)

# El Datepicker s'activa al template mitjansant un script de jQuery
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class PrincipiForm(forms.Form):
    principi = forms.CharField(max_length=100)

class ObjectiuForm(forms.Form):
	objectiu = forms.CharField(max_length=100)
	descripcio = forms.CharField(widget=forms.Textarea)

class ProjecteForm(forms.Form):
	projecte = forms.CharField(max_length=100)
	descripcio = forms.CharField(widget=forms.Textarea)
	presupost = forms.IntegerField()
	estat = forms.ChoiceField(required=False, 
		widget=forms.Select, choices=ESTAT)
	tipus = forms.ChoiceField(required=False, 
		widget=forms.Select, choices=TIPUS)
	data_inici = forms.DateField(widget=DateInput())
	data_fi = forms.DateField(widget=DateInput())
	vMin = forms.IntegerField()
	vMax = forms.IntegerField()

class MetricaForm(forms.Form):
	metrica = forms.CharField(max_length=100)
	descripcio = forms.CharField(widget=forms.Textarea)
	unitat = forms.CharField(max_length=100)
	vMin = forms.IntegerField()
	vMax = forms.IntegerField()
	objectiu = forms.ModelChoiceField(queryset=Objectiu.objects.exclude(), empty_label=None)