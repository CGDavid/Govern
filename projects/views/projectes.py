# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from projects.models import *
from projects.forms import *
from django.http import JsonResponse

# Projectes

# Retorna la view de la finestra de projectes, on es veuen tots el resources creats d'aquest tipus.
def projectes(request):
	projectes = Projecte.objects.all()
	return render(request, 'Projectes/projectes.html', {'projectes': projectes})

# Mostra el projecte corresponent a la id
def showProjecte(request, id):
	projecte = Projecte.objects.get(id=id)
	evaluacions = Evaluacio.objects.filter(projecte_id=id).order_by('creat')
	return render(request, 'Projectes/show.html', {'projecte': projecte, 'evaluacions' : evaluacions})

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
		'projecte_id': id }, projecte_id=id)
	return render(request, 'Projectes/editar.html', {'form': form, 'projecte_id': id})

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

# Lleva un objectiu del projecte (AJAX)
def llevaObjectiuP(request, id):
	if request.method == 'POST':
		if request.is_ajax():
			projecte = Projecte.objects.get(id=id)
			objectius_a_eliminar = request.POST.getlist('obj[]')[0].split(",")
			for obj in objectius_a_eliminar:
				projecte.objectiu.remove(Objectiu.objects.get(id=obj))
			return JsonResponse({"response" : "Objectiu eliminat!"})

# Afegeix un objectiu al projecte (AJAX)
def afegeixObjectiuP(request, id):
	if request.method == 'POST':
		if request.is_ajax():
			projecte = Projecte.objects.get(id=id)
			objectius_a_afegir = request.POST.getlist('obj[]')[0].split(",")
			for obj in objectius_a_afegir:
				projecte.objectiu.add(Objectiu.objects.get(id=obj))
			return JsonResponse({"response" : "Objectiu creat!"})

def crearEvaluacio(request, id):
	puntuacio_responsabilitat = request.POST['nota_responsabilitat']
	puntuacio_estrategia = request.POST['nota_estrategia']
	puntuacio_adquisicio = request.POST['nota_adquisicio']
	puntuacio_rendiment = request.POST['nota_rendiment']
	puntuacio_conformitat = request.POST['nota_conformitat']
	puntuacio_conducta = request.POST['nota_conducta']
	comentari_responsabilitat = request.POST['comentari_responsabilitat']
	comentari_estrategia = request.POST['comentari_estrategia']
	comentari_adquisicio = request.POST['comentari_adquisicio']
	comentari_rendiment = request.POST['comentari_rendiment']
	comentari_conformitat = request.POST['comentari_conformitat']
	comentari_conducta = request.POST['comentari_conducta']
	
	evaluacio = Evaluacio(
		puntuacio_responsabilitat=puntuacio_responsabilitat,
		puntuacio_estrategia=puntuacio_estrategia,
		puntuacio_adquisicio=puntuacio_adquisicio,
		puntuacio_rendiment=puntuacio_rendiment,
		puntuacio_conformitat=puntuacio_conformitat,
		puntuacio_conducta=puntuacio_conducta,
		comentari_responsabilitat=comentari_responsabilitat,
		comentari_estrategia=comentari_estrategia,
		comentari_adquisicio=comentari_adquisicio,
		comentari_rendiment=comentari_rendiment,
		comentari_conformitat=comentari_conformitat,
		comentari_conducta=comentari_conducta,
		projecte_id = id
		)
	evaluacio.save()

	return redirect('/projectes/'+id, args={'projecte_id':id})