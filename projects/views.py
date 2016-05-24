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
	principis = Principi.objects.all()
	return render(request, "Principis/principis.html", {'principis': principis})

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
			principis = Principi.objects.all()
			return render(request, 'Principis/principis.html', {'principis': principis})
	else:
		form = PrincipiForm()
	return render(request, 'Principis/crear.html', {'form': form})

# Elimina el principi corresponent a la id
def eliminaPrincipi(request, id):
	principi = Principi.objects.filter(id=id)
	principi.delete()
	principis = Principi.objects.all()
	return render(request, "Principis/principis.html", {'principis': principis})

# Edició del principi correponent a la id
def editaPrincipi(request, id):
	principi = Principi.objects.filter(id=id).values()[0]
	form = PrincipiForm(initial={'principi': principi.get('nom'), 'principi_id':id })
	return render(request, 'Principis/editar.html', {'form': form})

# Actualitza les dades d'un principi
def updatePrincipi(request):
	form = PrincipiForm(request.POST)
	if form.is_valid():
		nom = form.cleaned_data['principi']
		principi_id = form.cleaned_data['principi_id']
		principi = Principi.objects.filter(id=principi_id).update(nom=nom)
	principis = Principi.objects.all()
	return render(request, "Principis/principis.html", {'principis': principis})


# Objectius

# Retorna la view de la finestra d'objectius, on es veuen tots el resources creats d'aquest tipus.
def objectius(request):
	objectius = Objectiu.objects.all()
	metriques = Metrica.objects.all()
	return render(request, 'Objectius/objectius.html', {'objectius': objectius, 'metriques': metriques})

# Si el Request es GET, retorna la view de creació del resource amb el formulari buit.
# Si el Request es POST, crea el request amb les dades obtingudes al formulari
def crearObjectiu(request):
	if request.method == 'POST':
		form = ObjectiuForm(request.POST)
		if form.is_valid():
			# Si el formulari és vàlid, cream l'objectiu
			nom = form.cleaned_data['objectiu']
			descripcio = form.cleaned_data['descripcio']
			principis = form.cleaned_data['principis']
			o = Objectiu(nom=nom, descripcio=descripcio)
			o.save()
			# Afegim els principis
			for principi in principis:
				o.principis_objectius.add(principi)
			# Guardam l'objectiu
			o.save()
			objectius = Objectiu.objects.all()
			return render(request, 'Objectius/objectius.html', {'objectius': objectius})
	else:
		form = ObjectiuForm()
	return render(request, 'Objectius/crear.html', {'form': form})

# Elimina un objectiu corresponent a la id del argument
def eliminaObjectiu(request, id):
	objectiu = Objectiu.objects.filter(id=id)
	objectiu.delete()
	objectius = Objectiu.objects.all()
	return render(request, "Objectius/objectius.html", {'objectius': objectius})

# Edita un objectiu corresponent a la id del argument
def editaObjectiu(request, id):
	objectiu = Objectiu.objects.filter(id=id).values()[0]
	form = ObjectiuEditForm(initial={'objectiu': objectiu.get('nom'), 'descripcio': objectiu.get('descripcio'), 'objectiu_id':id })
	return render(request, 'Objectius/editar.html', {'form': form})

# Actualitza les dades d'un objectiu
def updateObjectiu(request):
	form = ObjectiuEditForm(request.POST)
	if form.is_valid():
		nom = form.cleaned_data['objectiu']
		descripcio = form.cleaned_data['descripcio']
		objectiu_id = form.cleaned_data['objectiu_id']
		objectiu = Objectiu.objects.filter(id=objectiu_id).update(nom=nom, descripcio=descripcio)
	objectius = Objectiu.objects.all()
	metriques = Metrica.objects.all()
	return render(request, "Objectius/objectius.html", {'objectius': objectius, 'metriques': metriques})


# Projectes

# Retorna la view de la finestra de projectes, on es veuen tots el resources creats d'aquest tipus.
def projectes(request):
	projectes = Projecte.objects.all()
	return render(request, 'Projectes/projectes.html', {'projectes': projectes})

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
			objectius = form.cleaned_data['objectius']
			vMin = form.cleaned_data['vMin']
			vMax = form.cleaned_data['vMax']
			p = Projecte(nom=nom, descripcio=descripcio, presupost=presupost, 
				estat=estat, tipus=tipus, data_inici=data_inici, data_fi=data_fi, 
				minim=vMin, maxim=vMax)
			p.save()
			# Afegim els objectius
			for objectiu in objectius:
				p.objectiu.add(objectiu)
			# Guardam el projecte
			p.save()
			projectes = Projecte.objects.all()
			return render(request, 'Projectes/projectes.html', {'projectes': projectes})
	else:
		form = ProjecteForm()
	return render(request, 'Projectes/crear.html', {'form': form})

def eliminaProjecte(request, id):
	projecte = Projecte.objects.filter(id=id)
	projecte.delete()
	projectes = Projecte.objects.all()
	return render(request, "Projectes/projectes.html", {'projectes': projectes})

# Edita un projecte corresponent a la id del argument
def editaProjecte(request, id):
	projecte = Projecte.objects.filter(id=id).values()[0]
	form = ProjecteEditForm(initial={
		'projecte': projecte.get('nom'), 
		'descripcio': projecte.get('descripcio'), 
		'presupost': projecte.get('presupost'), 
		'estat': projecte.get('estat'), 
		'tipus': projecte.get('tipus'), 
		'data_inici': projecte.get('data_inici'), 
		'data_fi': projecte.get('data_fi'), 
		'vMin': projecte.get('minim'), 
		'vMax': projecte.get('maxim'),
		'projecte_id': id })
	return render(request, 'Projectes/editar.html', {'form': form})

# Actualitza les dades d'un projecte
def updateProjecte(request):
	form = ProjecteEditForm(request.POST)
	if form.is_valid():
		nom = form.cleaned_data['projecte']
		descripcio = form.cleaned_data['descripcio']
		presupost = form.cleaned_data['presupost']
		estat = form.cleaned_data['estat']
		tipus = form.cleaned_data['tipus']
		data_inici = str(form.cleaned_data['data_inici'])
		data_fi = str(form.cleaned_data['data_fi'])
		vMin = form.cleaned_data['vMin']
		vMax = form.cleaned_data['vMax']
		projecte_id = form.cleaned_data['projecte_id']
		
		projecte = Projecte.objects.filter(id=projecte_id).update(
			nom=nom, 
			descripcio=descripcio, 
			presupost=presupost, 
			estat=estat, 
			tipus=tipus,
			data_inici=data_inici, 
			data_fi=data_fi, 
			maxim=vMin, 
			minim=vMax, 
			)
	projectes = Projecte.objects.all()
	return render(request, "Projectes/projectes.html", {'projectes': projectes})


# Mètriques

# Retorna la view de la finestra de mètriques, on es veuen tots el resources creats d'aquest tipus.
def metriques(request):
	metriques = Metrica.objects.all()
	return render(request, 'Metriques/metriques.html', {'metriques': metriques})

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
			m = Metrica(nom=nom, descripcio=descripcio, maxim=maxim, minim=minim, objectiu_id=objectiu_id, unitat=unitat)
			m.save()
			metriques = Metrica.objects.all()
			return render(request, 'Metriques/metriques.html', {'metriques': metriques})
	else:
		form = MetricaForm() 
	return render(request, 'Metriques/crear.html', {'form': form})

def eliminaMetrica(request, id):
	metrica = Metrica.objects.filter(id=id)
	metrica.delete()
	metriques = Metrica.objects.all()
	return render(request, "Metriques/metriques.html", {'metriques': metriques})

# Edita una mètrica corresponent a la id del argument
def editaMetrica(request, id):
	metrica = Metrica.objects.filter(id=id).values()[0]
	form = MetricaEditForm(initial={
		'metrica': metrica.get('nom'), 
		'descripcio': metrica.get('descripcio'),
		'unitat': metrica.get('unitat'),
		'vMin': metrica.get('minim'),
		'vMax': metrica.get('maxim'),
		'metrica_id': id })
	return render(request, 'Metriques/editar.html', {'form': form})

# Actualitza les dades d'una mètrica
def updateMetrica(request):
	form = MetricaEditForm(request.POST)
	if form.is_valid():
		nom = form.cleaned_data['metrica']
		descripcio = form.cleaned_data['descripcio']
		unitat = form.cleaned_data['unitat']
		vMin = form.cleaned_data['vMin']
		vMax = form.cleaned_data['vMax']
		metrica_id = form.cleaned_data['metrica_id']
		
		metrica = Metrica.objects.filter(id=metrica_id).update(
			nom=nom,
			descripcio=descripcio,
			unitat=unitat,
			minim=vMin,
			maxim=vMax
			)
	metriques = Metrica.objects.all()
	return render(request, "Metriques/metriques.html", {'metriques': metriques})