from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^principis$', views.principis, name='principis'),
    url(r'^principis/crear$', views.crearPrincipi, name='principis.crear'),
    url(r'^objectius$', views.objectius, name='objectius'),
    url(r'^objectius/crear$', views.crearObjectiu, name='objectius.crear'),
    url(r'^projectes$', views.projectes, name='projectes'),
    url(r'^projectes/crear$', views.crearProjecte, name='projectes.crear'),
    url(r'^metriques$', views.metriques, name='metriques'),
    url(r'^metriques/crear$', views.crearMetrica, name='metriques.crear'),
]
