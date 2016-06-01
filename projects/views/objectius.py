# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from projects.models import *
from projects.forms import *
from django.http import JsonResponse

# Objectius

# Retorna la view de la finestra d'objectius, on es veuen tots el resources creats d'aquest tipus.
def objectius(request):
	projectes = Projecte.objects.all()
	objectius = Objectiu.objects.all()
	metriques = Metrica.objects.all()
	
	return render(request, 'Objectius/objectius.html', {'objectius': objectius, 'metriques': metriques, 'projectes': projectes})

# Mostra l'objectiu corresponent a la id
def showObjectiu(request, id):
	objectiu = Objectiu.objects.get(id=id)
	projectes = objectiu.projectes_objectius.all()
	principis = objectiu.principis_objectius.all()
	metriques = Metrica.objects.filter(objectiu_id=id)

	# Obtener color del objetivo
	colorFinal = obtenirColor(metriques)

	return render(request, 'Objectius/show.html', {'objectiu': objectiu, 'principis': principis, 'metriques': metriques, 'colorFinal': colorFinal, 'projectes': projectes})

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
	form = ObjectiuEditForm(request.POST)
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

# Lleva un projecte del objectiu (AJAX)
def llevaProjecte(request, id):
	if request.method == 'POST':
		if request.is_ajax():
			objectiu = Objectiu.objects.get(id=id)
			projectes_a_eliminar = request.POST.getlist('obj[]')[0].split(",")
			for obj in projectes_a_eliminar:
				objectiu.projectes_objectius.remove(Projecte.objects.get(id=obj))
			return JsonResponse({"response" : "Projecte eliminat!"})

# Afegeix un projecte al objectiu (AJAX)
def afegeixProjecte(request, id):
	if request.method == 'POST':
		if request.is_ajax():
			objectiu = Objectiu.objects.get(id=id)
			projectes_a_afegir = request.POST.getlist('obj[]')[0].split(",")
			for obj in projectes_a_afegir:
				objectiu.projectes_objectius.add(Projecte.objects.get(id=obj))
			return JsonResponse({"response" : "Projecte creat!"})

def obtenirColor(metriques):
	# Si no tiene métricas, no lo pintamos
	if not metriques:
		return 'gris'

	valoresPonderados = []
	ponderacio_total = 0

	# Total de ponderaciones
	for metrica in metriques:
		ponderacio_total += float(metrica.ponderacio)

	# Calculamos qué porcentaje corresponde a cada metrica según su ponderación
	for metrica in metriques:
		# Obtenemos ponderación real de esta métrica
		ponderacio_real = metrica.ponderacio/ponderacio_total

		# Obtener color de metrica (rojo = 1, amarillo = 2, verde = 3)
		if metrica.valor < metrica.minim:
			# Rojo
			valor = 1
		elif metrica.valor < metrica.maxim:
			# Amarillo
			valor = 2
		elif metrica.valor > metrica.maxim:
			# Verde
			valor = 3

		valoresPonderados.append(valor*ponderacio_real)

	# Hacemos la media de los valores ponderados de las métricas
	valorFinal = 0
	for valor in valoresPonderados:
		valorFinal += valor

	# Rojo: 1 - 1,66666
	# Amarillo: 1,66667 - 2,33333
	# Verde: 2,33334 - 3
	if valorFinal <= 1.66666:
		colorFinal = 'rojo'
	elif valorFinal <= 2.33333:
		colorFinal = 'amarillo'
	elif valorFinal <= 3:
		colorFinal = 'verde'

	return colorFinal