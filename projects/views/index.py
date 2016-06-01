# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from projects.models import *
from projects.forms import *
from django.db.models import Sum
from .objectius import obtenirColor
import datetime, calendar

# Retorna la view del index de la aplicació
def index(request):
	objectius = Objectiu.objects.all()
	projectes_pendents = Projecte.objects.filter(estat='PE')
	projectes_en_curs = Projecte.objects.filter(estat='PR')
	nombre_projectes_en_curs = Projecte.objects.filter(estat='PR').count()
	inversions = []
	colors = []


	# Inversió total de cada objectiu
	for objectiu in objectius:
		# Els rebutjats no els contem
		inversions.append(objectiu.projectes_objectius.exclude(estat='RE').aggregate(Sum('presupost')).values()[0])

	# Color final de cada objectiu
	for objectiu in objectius:
		metrica = Metrica.objects.filter(objectiu_id=objectiu.id)
		colors.append(obtenirColor(metrica))
    
	return render(request, "index.html", 
		{
		 'objectius': objectius,
		 'inversions': inversions,
		 'colors': colors,
		 'pressupost_total' : pressupost_total(),
		 'passiu_total' : passiu_total(),
		 'nombre_projectes_en_curs': nombre_projectes_en_curs,
		 'projectes_pendents': projectes_pendents,
		 'projectes_en_curs':projectes_en_curs
		 })

# retorna el pressupost total de l'empresa
def pressupost_total():
	return 188216

# retorna el passiu d'aquest mes (suma dels pressupostos dels projectes que començen aquest mes)
def passiu_total():
	mes = datetime.datetime.now().month
	year = datetime.datetime.now().year
	ultim_dia = calendar.monthrange(year, mes)[1]
	start_date = datetime.datetime(year, mes, 1, 0, 0, 0, 0)
	end_date = datetime.datetime(year, mes, 1, 0, 0, 0, 0)

	return int(Projecte.objects.filter(data_inici__range=(start_date, end_date)).aggregate(Sum('presupost')).values()[0])