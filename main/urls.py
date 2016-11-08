from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Main, name='Main'),
    url(r'^cv', views.CV, name='CV'),
    url(r'^projets', views.CV, name='Projets'),
]
