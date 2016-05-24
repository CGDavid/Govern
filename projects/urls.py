from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^principis$', views.principis, name='principis'),
    url(r'^principis/crear$', views.crearPrincipi, name='principis.crear'),
    url(r'^principis/elimina/(?P<id>[0-9]+)$', views.eliminaPrincipi, name='principis.elimina'),
    url(r'^principis/edita/(?P<id>[0-9]+)$', views.editaPrincipi, name='principis.edita'),
    url(r'^principis/update$', views.updatePrincipi, name='principis.update'),
    url(r'^objectius$', views.objectius, name='objectius'),
    url(r'^objectius/crear$', views.crearObjectiu, name='objectius.crear'),
    url(r'^objectius/elimina/(?P<id>[0-9]+)$', views.eliminaObjectiu, name='objectius.elimina'),
    url(r'^objectius/edita/(?P<id>[0-9]+)$', views.editaObjectiu, name='objectius.edita'),
    url(r'^projectes$', views.projectes, name='projectes'),
    url(r'^projectes/crear$', views.crearProjecte, name='projectes.crear'),
    url(r'^projectes/elimina/(?P<id>[0-9]+)$', views.eliminaProjecte, name='projectes.elimina'),
    url(r'^projectes/edita/(?P<id>[0-9]+)$', views.editaProjecte, name='projectes.edita'),
    url(r'^metriques$', views.metriques, name='metriques'),
    url(r'^metriques/crear$', views.crearMetrica, name='metriques.crear'),
    url(r'^metriques/elimina/(?P<id>[0-9]+)$', views.eliminaMetrica, name='metriques.elimina'),
    url(r'^metriques/edita/(?P<id>[0-9]+)$', views.editaMetrica, name='metriques.edita'),
]
