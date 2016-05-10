# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

from .models import *

# A continuación 3 posibles variaciones de index. Se accede añadiendo /index2 o /index3 a la url

def index(request):
    project_list = Projecte.objects.order_by('modificat')
    view = {
        'project_list': project_list,
    }
    
    return render(request, "index.html",view)
