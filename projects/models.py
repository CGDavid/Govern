#! -- encoding: utf-8

from __future__ import unicode_literals
from django.core.validators import MaxValueValidator
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
    objectiu = models.ForeignKey(Objectiu, on_delete=models.CASCADE, null=True)
    puntuacio = models.FloatField()
    comentari = models.TextField()
    
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
    valoracio = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])
    projecte = models.ManyToManyField(Projecte, through='Historial')
    
    def __unicode__(self):
        return "%s" % (self.nom)


class Historial(models.Model):
    projecte = models.ForeignKey(Projecte, on_delete=models.CASCADE)
    principi = models.ForeignKey(Principi, on_delete=models.CASCADE, null=True) # A cumplir un objetivo!
    darrera_valoracio = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])
    
    def __unicode__(self):
        return "%s %s: %s" % (self.projecte, self.objectiu, self.darrera_valoracio)

