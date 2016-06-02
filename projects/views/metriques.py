# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from projects.models import *
from projects.forms import *

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
			valor = form.cleaned_data['valor']
			ponderacio = form.cleaned_data['ponderacio']
			objectiu_id = request.POST['objectiu']
			m = Metrica(nom=nom, descripcio=descripcio, maxim=maxim, minim=minim, valor=valor, objectiu_id=objectiu_id, unitat=unitat, ponderacio=ponderacio)
			m.save()
			metrica_id = m.id
			alertaMetrica(metrica_id)
			metriques = Metrica.objects.all()
			return render(request, 'Metriques/metriques.html', {'metriques': metriques})
	else:
		form = MetricaForm() 
	return render(request, 'Metriques/crear.html', {'form': form})

def eliminaMetrica(request, id):
	eliminaAlertaMetrica(id)
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
		'valor': metrica.get('valor'),
		'ponderacio': metrica.get('ponderacio'),
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
		valor = form.cleaned_data['valor']
		ponderacio = form.cleaned_data['ponderacio']
		metrica_id = form.cleaned_data['metrica_id']
		
		metrica = Metrica.objects.filter(id=metrica_id).update(
			nom=nom,
			descripcio=descripcio,
			unitat=unitat,
			minim=vMin,
			maxim=vMax,
			valor=valor,
			ponderacio=ponderacio
			)
	metriques = Metrica.objects.all()
	alertaMetrica(metrica_id)
	return render(request, "Metriques/metriques.html", {'metriques': metriques})

# Cream una alerta de la mètrica que correspon a la id
def alertaMetrica(id_metrica):
	metrica = Metrica.objects.get(id=id_metrica)
	metrica_nom = metrica.nom

	if metrica.valor < metrica.minim:
		color = 'R'
		descripcio = 'La metrica '+metrica_nom+' esta per sota del valor minim'
	elif metrica.valor < metrica.maxim:
		color = 'A'
		descripcio = 'La metrica '+metrica_nom+' esta entre valor minim i el maxim'
	elif metrica.valor >= metrica.maxim:
		color = 'V'
		descripcio = 'La metrica '+metrica_nom+' esta sobre el valor maxim'

	# Comprovam si existeix ja una alerta
	if metrica.alerta_metrica.all().exists():
		# Actualitzam l'alerta
		alerta = metrica.alerta_metrica.filter(tipus='ME').update(
				color = color,
				descripcio = descripcio
			)
	else:
		# Cream l'alerta
		alerta = Alerta(
					nom='Alerta metrica '+metrica_nom,
					descripcio=descripcio,
					uri='/metriques/edita/'+str(id_metrica),
					tipus='ME',
					color=color,
				)
		alerta.save()
		metrica.alerta_metrica.add(alerta)

# elimina una alerta d'una metrica que hem esborrat
def eliminaAlertaMetrica(id_metrica):
	metrica = Metrica.objects.get(id=id_metrica)
	for alerta in metrica.alerta_metrica.all():
		alerta.delete()
