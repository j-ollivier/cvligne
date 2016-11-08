from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post
from main.models import Navbar

# TODO :
# enhance categories dic entry to have a link to a page listing all posts including this category

def DevblogHome(request):
    context = {
        'img_archi_serveur':'/static/architecture_serveur.png',
        'style': '/static/style.css',
        'main_img': '/static/main_img.png',
        'navbar': Navbar.objects.all().order_by('uid'),
        'content': Post.objects.all(),
        'categories': [i[0] for i in Post.category_choices],
    }
    template = loader.get_template('devblog.html')
    return HttpResponse(template.render(
        context,request))