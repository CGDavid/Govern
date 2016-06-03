#! -- encoding: utf-8

from __future__ import unicode_literals
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone


class Objectiu(models.Model):
    nom = models.CharField(max_length=100)
    descripcio = models.TextField()
    
    def __unicode__(self):
        return "%s" % (self.nom)
        

class Projecte(models.Model):
    STATES = (
        ('PE','Pendent'),
        ('PR','Progres'),
        ('RE','Rebutjat'),
        ('FI','Finalitzat'),
    )
    
    TYPES = (
        ('F2P','Free To Play'),
        ('CO','Convencional'),
        ('ALT','Altres'),
    )

    nom = models.CharField(max_length=100)
    descripcio = models.TextField()
    presupost = models.FloatField()
    estat = models.CharField(max_length=2, choices=STATES)
    tipus = models.CharField(max_length=3, choices=TYPES, default='CO')
    objectiu = models.ManyToManyField(Objectiu, related_name="projectes_objectius")
    creat = models.DateTimeField(auto_now_add=True, null=True)
    modificat = models.DateTimeField(auto_now=True, null=True)
    data_inici = models.DateTimeField(null=True)
    data_fi = models.DateTimeField(null=True)
    minim = models.PositiveSmallIntegerField(null=True)
    
    def __unicode__(self):
        return "%s" % (self.nom)
        

class Metrica(models.Model):

    RANG = [(i,i) for i in range(11)]

    nom = models.CharField(max_length=100)
    descripcio = models.TextField()
    unitat = models.CharField(max_length=100)
    objectiu = models.ForeignKey(Objectiu, related_name="metriques_objectius")
    maxim = models.PositiveIntegerField(null=True)
    minim = models.PositiveIntegerField(null=True)
    valor = models.PositiveIntegerField(null=True)
    ponderacio = models.PositiveIntegerField(null=True, choices=RANG)
    
    def __unicode__(self):
        return "%s" % (self.nom)


class Principi(models.Model):
    nom = models.CharField(max_length=100)
    objectiu = models.ManyToManyField(Objectiu, related_name="principis_objectius")
    
    def __unicode__(self):
        return "%s" % (self.nom)


class Alerta(models.Model):

    TIPUS = (
        ('ME', 'Mètrica'),
        ('OB', 'Objectiu'),
        ('EV', 'Evaluació'),
    )

    COLOR = (
        ('R', 'rojo'),
        ('A', 'amarillo'),
        ('V', 'verde'),
    )

    projecte = models.ManyToManyField(Projecte, related_name="alerta_projecte")
    metrica = models.ManyToManyField(Metrica, related_name="alerta_metrica")
    descripcio = models.TextField()
    nom = models.CharField(max_length=100)
    uri = models.CharField(max_length=100)
    tipus = models.CharField(max_length=2, choices=TIPUS)
    color = models.CharField(max_length=1, choices=COLOR)
    
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
    
    creat = models.DateTimeField(auto_now_add=True, null=True)
    modificat = models.DateTimeField(auto_now=True, null=True)
    
    def _mitjana(self):
        """
        Retorna la mitjana de les puntuacions de l'Evaluacio
        
        returns: Float
        """
        puntuacions = [self.puntuacio_responsabilitat, self.puntuacio_estrategia]
        puntuacions.extend([self.puntuacio_adquisicio, self.puntuacio_rendiment])
        puntuacions.extend([self.puntuacio_conformitat, self.puntuacio_conducta])
        return float(sum(puntuacions))/len(puntuacions)
    mitjana = property(_mitjana)
        
    def __unicode__(self):
        return "Evaluació del projecte %s: %s. modificat el %s" % (self.projecte, self.mitjana, self.modificat)