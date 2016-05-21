from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^principis$', views.principis, name='principis'),
    url(r'^principis/crear$', views.crearPrincipi, name='principis'),
    url(r'^objectius$', views.objectius, name='objectius'),
    url(r'^objectius/crear$', views.crearObjectiu, name='objectius'),
    url(r'^projectes$', views.projectes, name='projectes'),
    url(r'^projectes/crear$', views.crearProjecte, name='projectes'),
    url(r'^grafiques$', views.grafiques, name='grafiques'),
]
