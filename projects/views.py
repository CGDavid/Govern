# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .models import *
from .forms import ProjectForm

# A continuación 3 posibles variaciones de index. Se accede añadiendo /index2 o /index3 a la url

def index(request):
    project_list = Projecte.objects.order_by('modificat')
    view = {
        'project_list': project_list,
    }
    
    return render(request, "index.html",view)


def project_new(request):
    if request.method == "POST":
        # print request.POST
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.creat = timezone.now()
            project.modificat = timezone.now()
            project.save()
            return redirect('index')
        else:
            # not valid
            print form
            return render(request, "forms/project_new.html")
    else:
        form = {
            'form' : ProjectForm(),
            'objectius' : Objectiu.objects.all(),
            'project_list': Projecte.objects.order_by('modificat'),
        }
    
    return render(request, "forms/project_new.html",form)


def project_edit(request):
    form = {
        'form' : ProjectForm(),
        'objectius' : Objectiu.objects.all(),
        'project_list': Projecte.objects.order_by('modificat'),
    }
    
    return render(request, "forms/project_edit.html",form)
