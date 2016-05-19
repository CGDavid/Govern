from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project/new/$', views.project_new, name='project_new'),
    url(r'^project/edit/$', views.project_edit, name='project_edit'),
]
