# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from projects.models import *
from projects.forms import *
from django.http import JsonResponse

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
	principi = Principi.objects.filter(id=id).values('nom')[0]
	form = PrincipiEditForm(initial={'principi': principi.get('nom'), 'principi_id':id }, principi_id=id)
	return render(request, 'Principis/editar.html', {'form': form, 'principi_id':id})

# Actualitza les dades d'un principi
def updatePrincipi(request):
	form = PrincipiForm(request.POST)
	if form.is_valid():
		nom = form.cleaned_data['principi']
		principi_id = form.data['principi_id']
		principi = Principi.objects.filter(id=principi_id).update(nom=nom)
		principis = Principi.objects.all()
	return render(request, "Principis/principis.html", {'principis': principis})

# Lleva un objectiu del principi (AJAX)
def llevaObjectiu(request, id):
	if request.method == 'POST':
		if request.is_ajax():
			principi = Principi.objects.get(id=id)
			objectius_a_eliminar = request.POST.getlist('obj[]')[0].split(",")
			for obj in objectius_a_eliminar:
				principi.objectiu.remove(Objectiu.objects.get(id=obj))
			return JsonResponse({"response" : "Objectiu eliminat!"})

# Afegeix un objectiu al principi (AJAX)
def afegeixObjectiu(request, id):
	if request.method == 'POST':
		if request.is_ajax():
			principi = Principi.objects.get(id=id)
			objectius_a_afegir = request.POST.getlist('obj[]')[0].split(",")
			for obj in objectius_a_afegir:
				principi.objectiu.add(Objectiu.objects.get(id=obj))
			return JsonResponse({"response" : "Objectiu creat!"})