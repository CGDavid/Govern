#! -- encoding: utf-8

from __future__ import unicode_literals

from django.db import models


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
    
    def __unicode__(self):
        return "%s %s" % (self.nom, self.estat)

class Valoracio(models.Model):
    projecte = models.ForeignKey(Projecte, on_delete=models.CASCADE)
    objectiu = models.ForeignKey(Objectiu, on_delete=models.CASCADE)
    puntuacio = models.FloatField()
    comentari = models.TextField()


class Metrica(models.Model):
    UNITATS = (
        ('EUR','Euros'),
        ('DIA','Dies'),
        ('PCT','Percentatge')
    )
    nom = models.CharField(max_length=30)
    descripcio = models.TextField()
    unitat = models.CharField(max_length=2, choices=UNITATS)
    objectiu = models.ForeignKey(Objectiu, related_name="metriques_objectius")
    
    def __unicode__(self):
        return "%s %s" % (self.nom, self.descripcio)