# -*- coding: utf-8 -*-

import os
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import About, TeylaGroup, Project, News, Stuff, Document, Requisites, GeneralInfo
from django.core.paginator import Paginator


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
        'stuff': Stuff.objects.all(),
        'news': News.objects.order_by('-date', '-id')[:3],
        'projects': Project.objects.order_by('-id')[:3],
        'ginfo': GeneralInfo.objects.first()
    }
    return render(req, 'tengApp/home.html', context)


def business_group(req):
    pagntor = Paginator(TeylaGroup.objects.all(), 3)
    context = {
        'teyla_group': [pagntor.page(number).object_list for number in pagntor.page_range],
        'ginfo': GeneralInfo.objects.first()
    }
    return render(req, 'tengApp/business_group.html', context)


def about(req):
    info = About.objects.all()
    pagntor = Paginator(Document.objects.all(), 3)
    context = {
        'about': info.get(code='about'),
        'docs': [pagntor.page(number).object_list for number in pagntor.page_range],
        'requisites': Requisites.objects.first(),
        'contacts': ''
    }
    return render(req, 'tengApp/about.html', context)


def project(req):
    return render(req, 'tengApp/project.html')


def news(req):
    return render(req, 'tengApp/news.html')


def media(req, path):
    file_name = os.path.join(settings.MEDIA_ROOT, path)
    _, file_ext = os.path.splitext(file_name)

    # todo: заменить эту цепочку if-ов на словарь
    content_type = 'image/jpeg'  # default value
    if file_ext.lower() in ('.jpg', '.jpeg'):
        content_type = 'image/jpeg'
    if file_ext.lower() in ('.png',):
        content_type = 'image/png'
    if file_ext.lower() in ('.pdf',):
        content_type = 'application/pdf'
    if file_ext.lower() in ('.txt',):
        content_type = 'text/plain'
    if file_ext.lower() in ('.doc', '.docx'):
        content_type = 'application/octet-stream'

    image_data = open(file_name, 'rb').read()
    return HttpResponse(image_data, content_type=content_type)
