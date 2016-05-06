#! -- encoding: utf-8

from __future__ import unicode_literals
from django.core.validators import MaxValueValidator
from django.db import models
from datetime import datetime


class Objectiu(models.Model):
    nom = models.CharField(max_length=30)
    descripcio = models.TextField()
    
    def __unicode__(self):
        return "%s %s" % (self.nom, self.descripcio)
        

class Projecte(models.Model):
    STATES = (
        ('PE','Pendent'),
        ('PR','Progres'),
        ('RE','Rebutjat'),
        ('FI','Finalitzat'),
    )
    nom = models.CharField(max_length=30)
    descripcio = models.TextField()
    presupost = models.FloatField()
    estat = models.CharField(max_length=2, choices=STATES)
    objectiu = models.ManyToManyField(Objectiu, through='Valoracio')
    creat = models.DateTimeField(auto_now_add=True, blank=True)
    modificat = models.DateTimeField(auto_now=True, blank=True)
    
    def __unicode__(self):
        return "%s %s" % (self.nom, self.estat)
        

class Valoracio(models.Model):
    projecte = models.ForeignKey(Projecte, on_delete=models.CASCADE)
    objectiu = models.ForeignKey(Objectiu, on_delete=models.CASCADE, null=True)
    puntuacio = models.FloatField()
    comentari = models.TextField()
    creat = models.DateTimeField(auto_now_add=True, blank=True)
    modificat = models.DateTimeField(auto_now=True, blank=True)
    
    def __unicode__(self):
        return "%s %s: %s" % (self.projecte, self.objectiu, self.puntuacio)


class Metrica(models.Model):
    UNITATS = (
        ('EUR','Euros'),
        ('DIA','Dies'),
        ('PCT','Percentatge')
    )
    nom = models.CharField(max_length=30)
    descripcio = models.TextField()
    unitat = models.CharField(max_length=11, choices=UNITATS)
    objectiu = models.ForeignKey(Objectiu, related_name="metriques_objectius")
    
    def __unicode__(self):
        return "%s %s" % (self.nom, self.descripcio)


class Principi(models.Model):
    nom = models.CharField(max_length=30)
    objectiu = models.ManyToManyField(Objectiu, related_name="principis_objectius")
    
    def __unicode__(self):
        return "%s" % (self.nom)


class Evaluacio(models.Model):
    projecte = models.ForeignKey(Projecte, on_delete=models.CASCADE)
    
    # puntuacions
    puntuacio_responsabilitat = models.PositiveSmallIntegerField()
    puntuacio_estrategia = models.PositiveSmallIntegerField()
    puntuacio_adquisicio = models.PositiveSmallIntegerField()
    puntuacio_rendiment = models.PositiveSmallIntegerField()
    puntuacio_conformitat = models.PositiveSmallIntegerField()
    puntuacio_conducta = models.PositiveSmallIntegerField()
    
    # comentaris
    comentari_responsabilitat = models.TextField()
    comentari_estrategia = models.TextField()
    comentari_adquisicio = models.TextField()
    comentari_rendiment = models.TextField()
    comentari_conformitat = models.TextField()
    comentari_conducta = models.TextField()
    
    creat = models.DateTimeField(auto_now_add=True, blank=True)
    modificat = models.DateTimeField(auto_now=True, blank=True)
    
    def __unicode__(self):
        return "Evaluació del projecte %s. %s" % (self.projecte, self.modificat)

