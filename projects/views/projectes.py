# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from projects.models import *
from projects.forms import *

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