from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),

    # Views principis
    url(r'^principis$', views.principis, name='principis'),
    url(r'^principis/crear$', views.crearPrincipi, name='principis.crear'),
    url(r'^principis/elimina/(?P<id>[0-9]+)$', views.eliminaPrincipi, name='principis.elimina'),
    url(r'^principis/edita/(?P<id>[0-9]+)$', views.editaPrincipi, name='principis.edita'),
    url(r'^principis/update$', views.updatePrincipi, name='principis.update'),

    # Views objectius
    url(r'^objectius$', views.objectius, name='objectius'),
    url(r'^objectius/crear$', views.crearObjectiu, name='objectius.crear'),
    url(r'^objectius/elimina/(?P<id>[0-9]+)$', views.eliminaObjectiu, name='objectius.elimina'),
    url(r'^objectius/edita/(?P<id>[0-9]+)$', views.editaObjectiu, name='objectius.edita'),
    url(r'^objectius/update$', views.updateObjectiu, name='objectius.update'),

    # Views projectes
    url(r'^projectes$', views.projectes, name='projectes'),
    url(r'^projectes/(?P<id>[0-9]+)$', views.showProjecte, name='projectes.mostra'),
    url(r'^projectes/crear$', views.crearProjecte, name='projectes.crear'),
    url(r'^projectes/elimina/(?P<id>[0-9]+)$', views.eliminaProjecte, name='projectes.elimina'),
    url(r'^projectes/edita/(?P<id>[0-9]+)$', views.editaProjecte, name='projectes.edita'),
    url(r'^projectes/update$', views.updateProjecte, name='projectes.update'),

    # Views metriques
    url(r'^metriques$', views.metriques, name='metriques'),
    url(r'^metriques/crear$', views.crearMetrica, name='metriques.crear'),
    url(r'^metriques/elimina/(?P<id>[0-9]+)$', views.eliminaMetrica, name='metriques.elimina'),
    url(r'^metriques/edita/(?P<id>[0-9]+)$', views.editaMetrica, name='metriques.edita'),
    url(r'^metriques/update$', views.updateMetrica, name='metriques.update'),
    
    # Form edit principis
    url(r'^lleva/objectiu/(?P<id>[0-9]+)$', views.llevaObjectiu, name='principis.llevaObjectiu'),
    url(r'^afegeix/objectiu/(?P<id>[0-9]+)$', views.afegeixObjectiu, name='principis.afegeixObjectiu'),   

    # Form edit objectius
    url(r'^lleva/principi/(?P<id>[0-9]+)$', views.llevaPrincipi, name='objectius.llevaPrincipi'),
    url(r'^afegeix/principi/(?P<id>[0-9]+)$', views.afegeixPrincipi, name='objectius.afegeixPrincipi'),
    url(r'^afegeix/projecte/(?P<id>[0-9]+)$', views.afegeixProjecte, name='objectius.afegeixProjecte'),   
    url(r'^lleva/projecte/(?P<id>[0-9]+)$', views.llevaProjecte, name='objectius.llevaProjecte'),   
    url(r'^lleva/metrica/(?P<id>[0-9]+)$', views.llevaMetrica, name='objectius.llevaMetrica'),

    # Form edit projectes
    url(r'^afegeix/objectiu/projecte/(?P<id>[0-9]+)$', views.afegeixObjectiuP, name='projectes.afegeixPrincipi'),
    url(r'^lleva/objectiu/projecte/(?P<id>[0-9]+)$', views.llevaObjectiuP, name='projectes.llevaMetrica'),

    # Crear evaluacio
    url(r'^evaluacio/crear/(?P<id>[0-9]+)$', views.crearEvaluacio, name='evaluacio.crearEvaluacio'),
]
