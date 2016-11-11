from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CV, name='CV'),
    url(r'^cv/', views.CV, name='CV'),
    url(r'^projets/', views.Projets, name='Projets'),
    url(r'^focus/(?P<project_uid>\d+)', views.ProjetFocus, name='focus'),
]
