# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

from .models import *

# A continuación 3 posibles variaciones de index. Se accede añadiendo /index2 o /index3 a la url

def index(request):
    return render(request, "index.html")

# Principis
def principis(request):    
    return render(request, "Principis/principis.html")

def crearPrincipi(request):    
    return render(request, "Principis/crear.html")

# Objectius
def objectius(request):
    return render(request, "Objectius/objectius.html")

def crearObjectiu(request):    
    return render(request, "Objectius/crear.html")

# Projectes
def projectes(request):
    return render(request, "Projectes/projectes.html")

def crearProjecte(request):    
    return render(request, "Projectes/crear.html")

# Gràfiques
def grafiques(request):
    return render(request, "Grafiques/grafiques.html")