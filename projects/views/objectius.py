# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from projects.models import *
from projects.forms import *
from django.http import JsonResponse

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
	form = ObjectiuEditForm(initial={'objectiu': objectiu.get('nom'), 'descripcio': objectiu.get('descripcio'), 'objectiu_id':id }, objectiu_id=id)
	return render(request, 'Objectius/editar.html', {'form': form, 'objectiu_id': id})

# Actualitza les dades d'un objectiu
def updateObjectiu(request):
	form = ObjectiuForm(request.POST)
	if form.is_valid():
		nom = form.cleaned_data['objectiu']
		descripcio = form.cleaned_data['descripcio']
		objectiu_id = form.cleaned_data['objectiu_id']
		objectiu = Objectiu.objects.filter(id=objectiu_id).update(nom=nom, descripcio=descripcio)
	objectius = Objectiu.objects.all()
	metriques = Metrica.objects.all()
	return render(request, "Objectius/objectius.html", {'objectius': objectius, 'metriques': metriques})

# Lleva un principi del objectiu (AJAX)
def llevaPrincipi(request, id):
	if request.method == 'POST':
		if request.is_ajax():
			objectiu = Objectiu.objects.get(id=id)
			principis_a_eliminar = request.POST.getlist('obj[]')[0].split(",")
			for obj in principis_a_eliminar:
				objectiu.principis_objectius.remove(Principi.objects.get(id=obj))
			return JsonResponse({"response" : "Principi eliminat!"})

# Afegeix un principi al objectiu (AJAX)
def afegeixPrincipi(request, id):
	if request.method == 'POST':
		if request.is_ajax():
			objectiu = Objectiu.objects.get(id=id)
			principis_a_afegir = request.POST.getlist('obj[]')[0].split(",")
			for obj in principis_a_afegir:
				objectiu.principis_objectius.add(Principi.objects.get(id=obj))
			return JsonResponse({"response" : "Principi creat!"})

# Lleva una metrica del objectiu (AJAX)
def llevaMetrica(request, id):
	if request.method == 'POST':
		if request.is_ajax():
			objectiu = Objectiu.objects.get(id=id)
			metriques_a_eliminar = request.POST.getlist('obj[]')[0].split(",")
			for obj in metriques_a_eliminar:
				Metrica.objects.get(id=obj).delete()
			return JsonResponse({"response" : "Principi eliminat!"})