# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

# A continuación 3 posibles variaciones de index. Se accede añadiendo /index2 o /index3 a la url

def index(request):
    return render(request, "index.html")