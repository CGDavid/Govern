from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index2/', views.index2, name='index2'),
    url(r'^index3/', views.index3, name='index3'),
]
