# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from projects.models import *
from projects.forms import *

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
