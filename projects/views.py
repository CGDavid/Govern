# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import *
from .forms import *

# Retorna la view del index de la aplicació
def index(request):
    return render(request, "index.html")


# Principis

# Retorna la view de la finestra de principis, on es veuen tots el resources creats d'aquest tipus.
def principis(request):    
    return render(request, "Principis/principis.html")

# Si el Request es GET, retorna la view de creació del resource amb el formulari buit.
# Si el Request es POST, crea el request amb les dades obtingudes al formulari
def crearPrincipi(request):
	if request.method == 'POST':
		form = PrincipiForm(request.POST)
		if form.is_valid():
			# Si el formulari és vàlid, cream el principi
			nom = form.cleaned_data['principi']
			p = Principi(nom=nom)
			p.save()
			return render(request, 'index.html')
	else:
		form = PrincipiForm()
	return render(request, 'Principis/crear.html', {'form': form})


# Objectius

# Retorna la view de la finestra d'objectius, on es veuen tots el resources creats d'aquest tipus.
def objectius(request):
    return render(request, 'Objectius/objectius.html')

# Si el Request es GET, retorna la view de creació del resource amb el formulari buit.
# Si el Request es POST, crea el request amb les dades obtingudes al formulari
def crearObjectiu(request):
	if request.method == 'POST':
		form = ObjectiuForm(request.POST)
		if form.is_valid():
			# Si el formulari és vàlid, cream l'objectiu
			nom = form.cleaned_data['objectiu']
			descripcio = form.cleaned_data['descripcio']
			o = Objectiu(nom=nom, descripcio=descripcio)
			o.save()
			return render(request, 'index.html')
	else:
		form = ObjectiuForm()
	return render(request, 'Objectius/crear.html', {'form': form})


# Projectes

# Retorna la view de la finestra de projectes, on es veuen tots el resources creats d'aquest tipus.
def projectes(request):
    return render(request, 'Projectes/projectes.html')

# Si el Request es GET, retorna la view de creació del resource amb el formulari buit.
# Si el Request es POST, crea el request amb les dades obtingudes al formulari
def crearProjecte(request):
	if request.method == 'POST':
		form = ProjecteForm(request.POST)
		if form.is_valid():
			# Si el formulari és vàlid, cream el projecte
			nom = form.cleaned_data['projecte']
			descripcio = form.cleaned_data['descripcio']
			presupost = form.cleaned_data['presupost']
			estat = form.cleaned_data['estat']
			tipus = form.cleaned_data['tipus']
			data_inici = str(form.cleaned_data['data_inici'])
			data_fi = str(form.cleaned_data['data_fi'])
			vMin = form.cleaned_data['vMin']
			vMax = form.cleaned_data['vMax']
			p = Projecte(nom=nom, descripcio=descripcio, presupost=presupost, 
				estat=estat, tipus=tipus, data_inici=data_inici, data_fi=data_fi, 
				minim=vMin, maxim=vMax)
			p.save()
			return render(request, 'index.html')
	else:
		form = ProjecteForm()
	return render(request, 'Projectes/crear.html', {'form': form})


# Mètriques

# Retorna la view de la finestra de mètriques, on es veuen tots el resources creats d'aquest tipus.
def metriques(request):
    return render(request, 'Metriques/metriques.html')

# Si el Request es GET, retorna la view de creació del resource amb el formulari buit.
# Si el Request es POST, crea el request amb les dades obtingudes al formulari
def crearMetrica(request):
	if request.method == 'POST':
		form = MetricaForm(request.POST)
		if form.is_valid():
			# Si el formulari és vàlid, cream la métrica
			nom = form.cleaned_data['metrica']
			descripcio = form.cleaned_data['descripcio']
			unitat = form.cleaned_data['unitat']
			maxim = form.cleaned_data['vMax']
			minim = form.cleaned_data['vMin']
			objectiu_id = request.POST['objectiu']
			m = Metrica(nom=nom, descripcio=descripcio, maxim=maxim, minim=minim, objectiu_id=objectiu_id)
			m.save()
			return render(request, 'index.html')
	else:
		form = MetricaForm() 
	return render(request, 'Metriques/crear.html', {'form': form})