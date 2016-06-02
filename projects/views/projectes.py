# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from projects.models import *
from projects.forms import *
from django.http import JsonResponse
from django.db.models import Avg

# Projectes

# Retorna la view de la finestra de projectes, on es veuen tots el resources creats d'aquest tipus.
def projectes(request):
	projectes = Projecte.objects.all()
	return render(request, 'Projectes/projectes.html', {'projectes': projectes})

# Mostra el projecte corresponent a la id
def showProjecte(request, projecte_id):
	nota_mitjana = mitjanaEvaluacio(projecte_id)
	projecte = Projecte.objects.get(id=projecte_id)
	objectius = Objectiu.objects.all()
	evaluacions = Evaluacio.objects.filter(projecte_id=projecte_id).order_by('creat')
	return render(request, 'Projectes/show.html', {'projecte': projecte, 'evaluacions' : evaluacions, 'objectius': objectius, 'nota_mitjana': nota_mitjana})

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
			estat = 'PE'
			tipus = form.cleaned_data['tipus']
			data_inici = str(form.cleaned_data['data_inici'])
			data_fi = str(form.cleaned_data['data_fi'])
			vMin = form.cleaned_data['vMin']
			p = Projecte(nom=nom, descripcio=descripcio, presupost=presupost, 
				estat=estat, tipus=tipus, data_inici=data_inici, data_fi=data_fi, 
				minim=vMin)
			p.save()

			projectes = Projecte.objects.all()
			return render(request, 'Projectes/projectes.html', {'projectes': projectes})
	else:
		form = ProjecteForm()
	return render(request, 'Projectes/crear.html', {'form': form})

def eliminaProjecte(request, id):
	eliminaAlertaProjecte(id)
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
		projecte_id = form.cleaned_data['projecte_id']
		
		projecte = Projecte.objects.filter(id=projecte_id).update(
			nom=nom,
			descripcio=descripcio,
			presupost=presupost,
			estat=estat,
			tipus=tipus,
			data_inici=data_inici,
			data_fi=data_fi,
			minim=vMin,
			)

		#Comprovam si s'han modificat els objectius per afegir o eliminar una alerta
		checkAlertaObjectius(projecte_id)
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

	# Check per comprovar si la mitjana d'evaluacions es major o menor que el minim (si es menor cream alerta)
	alertaEvaluacio(id)

	return redirect('/projectes/'+id, args={'projecte_id':id})

# Elimina la evaluació corresponent a evaluacio_id
def eliminaEvaluacio(request, projecte_id, evaluacio_id):
	Evaluacio.objects.filter(id=evaluacio_id).delete()

	# Check per comprovar si la mitjana d'evaluacions es major o menor que el minim (si es menor cream alerta)
	checkAlertaEvaluacio(id)

	return redirect('/projectes/'+projecte_id, args={'projecte_id':projecte_id})

# Acceptar projecte corresponent a la id
def acceptaProjecte(request):
	id_projecte = request.POST['id_projecte']
	projecte = Projecte.objects.get(id=id_projecte) 
	objectius = request.POST.getlist('objectius')
	# Si no hi ha objectius cream una alerta
	if not objectius:
		alertaObjectius(id_projecte)
	else:
		for objectiu in objectius:
			projecte.objectiu.add(objectiu)
	projecte.estat = 'PR'
	projecte.save()
	return redirect('/projectes/'+id_projecte, args={'projecte_id':id_projecte})

# Rebutjar projecte corresponent a la id
def rebutjaProjecte(request, id):
	Projecte.objects.filter(id=id).update(estat='RE')
	return redirect('/projectes/'+id, args={'projecte_id':id})


# Genera una alerta quan un projecte no està alineat amb cap objectiu
def alertaObjectius(id_projecte):
	projecte = Projecte.objects.get(id=id_projecte)
	nomProjecte = projecte.nom
	alerta = Alerta(
			nom='Alerta projecte '+nomProjecte,
			uri='/projectes/'+id_projecte,
			tipus='OB',
			color='R',
			descripcio='El projecte '+nomProjecte+' no te cap objectiu associat'
		)
	alerta.save()
	alerta.projecte.add(projecte)

# Checkeam si s'ha d'eliminar o crear una alerta nova degut a un update
def checkAlertaObjectius(projecte_id):
	projecte = Projecte.objects.get(id=projecte_id)
	if not projecte.objectiu.all():
		alertaObjectius(projecte_id)
	else:
		for alerta in projecte.alerta_projecte.filter(tipus='OB'):
			alerta.delete()

# Treu la nota mitjana de totes les notes de totes les evaluacions
def mitjanaEvaluacio(projecte_id):
	if Evaluacio.objects.filter(projecte_id=projecte_id).exists():
		evaluacio = Evaluacio.objects.filter(projecte_id=projecte_id).order_by('creat').last()
		nota_estrategia = evaluacio.puntuacio_estrategia
		nota_adquisicio = evaluacio.puntuacio_adquisicio
		nota_conformitat = evaluacio.puntuacio_conformitat
		nota_conducta = evaluacio.puntuacio_conducta
		nota_responsabilitat = evaluacio.puntuacio_responsabilitat
		nota_rendiment = evaluacio.puntuacio_rendiment
		nota_total = float(nota_estrategia+nota_adquisicio+nota_conformitat+nota_conducta+nota_responsabilitat+nota_rendiment)
		nota_mitjana = nota_total/6
	else:
		nota_mitjana = 'N/A'
	return nota_mitjana

# Cream una alerta d'un projecte quan la seva evaluació està sota vMin
def alertaEvaluacio(id_projecte):
	mitjana = mitjanaEvaluacio(id_projecte)
	projecte = Projecte.objects.get(id=id_projecte)
	nomProjecte = projecte.nom
	if mitjana != 'N/A':
		if mitjana < projecte.minim:
			if not projecte.alerta_projecte.filter(tipus='EV'):
				alerta = Alerta(
					nom='Alerta projecte '+nomProjecte,
					uri='/projectes/'+id_projecte,
					tipus='EV',
					color='R',
					descripcio='El projecte '+nomProjecte+' te una valoracio per sota la valoracio minima'
				)
				alerta.save()
				projecte.alerta_projecte.add(alerta)
		else:
			for alerta in projecte.alerta_projecte.filter(tipus='EV'):
				alerta.delete()

# Elimina les alertes d'un projecte esborrat
def eliminaAlertaProjecte(id_projecte):
	projecte = Projecte.objects.get(id=id_projecte)
	for alerta in projecte.alerta_projecte.all():
		alerta.delete()