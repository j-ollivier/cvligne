from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Navbar


def Main(request):
    context = {
        'style': '/static/style.css',
        'main_img': '/static/main_img.png',
        'navbar': Navbar.objects.all().order_by('uid'),
        'content': '/static/wip.png'
    }
    template = loader.get_template('accueil.html')
    return HttpResponse(template.render(context,request))

def CV(request):
    context = {
        'style': '/static/style.css',
        'main_img': '/static/main_img.png',
        'navbar': Navbar.objects.all().order_by('uid'),
        'content': '/static/wip.png'
    }
    template = loader.get_template('cv.html')
    return HttpResponse(template.render(context,request))

def Projets(request):
    context = {
        'style': '/static/style.css',
        'main_img': '/static/main_img.png',
        'navbar': Navbar.objects.all().order_by('uid'),
        'content': '/static/wip.png'
    }
    template = loader.get_template('projets.html')
    return HttpResponse(template.render(context,request))