# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import *
from .forms import *

# A continuación 3 posibles variaciones de index. Se accede añadiendo /index2 o /index3 a la url

def index(request):
    return render(request, "index.html")

# Principis
def principis(request):    
    return render(request, "Principis/principis.html")

def crearPrincipi(request):
	# Dades enviades desde el form
	if request.method == 'POST':
		form = PrincipiForm(request.POST)
		if form.is_valid():
			# Si el formulari és vàlid, cream el principi
			nom = form.cleaned_data['principi']
			p = Principi(nom=nom)
			p.save()
			return render(request, 'index.html')
	# Request de view de formulari
	else:
		form = PrincipiForm()
	return render(request, 'Principis/crear.html', {'form': form})

# Objectius
def objectius(request):
    return render(request, 'Objectius/objectius.html')

def crearObjectiu(request):
	# Dades enviades desde el form
	if request.method == 'POST':
		form = ObjectiuForm(request.POST)
		if form.is_valid():
			# Si el formulari és vàlid, cream el objectiu
			nom = form.cleaned_data['objectiu']
			descripcio = form.cleaned_data['descripcio']
			o = Objectiu(nom=nom, descripcio=descripcio)
			o.save()
			return render(request, 'index.html')
	# Request de view de formulari
	else:
		form = ObjectiuForm()
	return render(request, 'Objectius/crear.html', {'form': form})

# Projectes
def projectes(request):
    return render(request, 'Projectes/projectes.html')

def crearProjecte(request):
	# Dades enviades desde el form
	if request.method == 'POST':
		form = PrincipiForm(request.POST)
		if form.is_valid():
			# Si el formulari és vàlid, cream el objectiu
			
			return render(request, 'index.html')
	# Request de view de formulari
	else:
		form = PrincipiForm()
	return render(request, 'Projectes/crear.html', {'form': form})

# Mètriques
def metriques(request):
    return render(request, 'Metriques/metriques.html')

def crearMetrica(request):
	# Dades enviades desde el form
	if request.method == 'POST':
		form = MetricaForm(request.POST)
		if form.is_valid():
			# Si el formulari és vàlid, cream el objectiu
			nom = form.cleaned_data['metrica']
			descripcio = form.cleaned_data['descripcio']
			unitat = form.cleaned_data['unitat']
			maxim = form.cleaned_data['vMax']
			minim = form.cleaned_data['vMin']
			objectiu_id = request.POST['objectiu']
			m = Metrica(nom=nom, descripcio=descripcio, maxim=maxim, minim=minim, objectiu_id=objectiu_id)
			m.save()
			return render(request, 'index.html')
	# Request de view de formulari
	else:
		form = MetricaForm() 
	return render(request, 'Metriques/crear.html', {'form': form})