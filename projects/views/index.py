# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from projects.models import *
from projects.forms import *

# Retorna la view del index de la aplicació
def index(request):
    return render(request, "index.html")