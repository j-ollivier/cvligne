from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Navbar, ExpTable, FormationTable, Projects, ProjectsDocs, FooterItems


def CV(request):
    context = {
        'style': '/static/style_season.css',
        'main_img': '/static/main_img.png',
        'navbar': Navbar.objects.all().order_by('uid'),
        'exp_table': ExpTable.objects.all().order_by('name'),
        'formation_table': FormationTable.objects.all().order_by('uid'),
        'footer_items': FooterItems.objects.all().order_by('uid'),
    }
    template = loader.get_template('cv.html')
    return HttpResponse(template.render(context,request))

def Projets(request):
    context = {
        'style': '/static/style_season.css',
        'main_img': '/static/main_img.png',
        'navbar': Navbar.objects.all().order_by('uid'),
        'pdf_icon': '/static/pdf_icon.png',
        'project_qs': Projects.objects.prefetch_related('docs_set').all().order_by('uid'),
        'img_archi_serveur':'/static/architecture_serveur.png',
        'footer_items': FooterItems.objects.all().order_by('uid'),
        'back_link_text': 'Haut de page',
    }

    template = loader.get_template('projets.html')
    return HttpResponse(template.render(context,request))

def ProjetFocus(request, project_uid):
    # Making a liste from the project_uid string received
    project_uid = project_uid.split(',')
    context = {
        'style': '/static/style_season.css',
        'main_img': '/static/main_img.png',
        'navbar': Navbar.objects.all().order_by('uid'),
        'pdf_icon': '/static/pdf_icon.png',
        'project_qs': Projects.objects.prefetch_related('docs_set').filter(uid__in= project_uid),
        'footer_items': FooterItems.objects.all().order_by('uid'),
        'back_link_text': 'Retour à la liste des projets',
    }

    template = loader.get_template('projets.html')
    return HttpResponse(template.render(context,request))