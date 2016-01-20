import os
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import About, TeylaGroup, Project, News, Stuff, Document, Requisites


def home(req):
    info = About.objects.all()
    info_block = {
        'about': info.get(code='about'),  # for 'code' see About.CODE_CHOICE property
        'docs': info.get(code='docs'),
        'requisites': info.get(code='requisites'),
        'contacts': info.get(code='contacts')
    }
    context = {
        'info_block': info_block,
        'stuff': Stuff.objects.all()
    }
    return render(req, 'tengApp/home.html', context)


def business_group(req):
    return render(req, 'tengApp/business_group.html')


def about(req):
    return render(req, 'tengApp/about.html')


def project(req):
    return render(req, 'tengApp/project.html')


def news(req):
    return render(req, 'tengApp/news.html')


def media(req, path):
    file_name = os.path.join(settings.MEDIA_ROOT, path)
    _, file_ext = os.path.splitext(file_name)

    content_type = 'image/jpeg'  # default value
    if file_ext.lower() in ('.jpg', '.jpeg'):
        content_type = 'image/jpeg'
    if file_ext.lower() in ('.png',):
        content_type = 'image/png'

    image_data = open(file_name, 'rb').read()
    return HttpResponse(image_data, content_type=content_type)
