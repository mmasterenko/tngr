# -*- coding: utf-8 -*-

import os
from utils import group_list
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
from django.core.paginator import Paginator
from .local_settings import NEWS_PER_PAGE
from .models import AboutContact, AboutPageSettings, Actions, ProjectPageSettings, ProjectArea, \
    Project, TeylaGroup, Requisites, Settings, News, BusinessPageSettings, MainPageSettings, GeneralInfo, \
    Document, Stuff, FlatPages, AboutCompany, AboutContacts, AboutRequisites, AboutDocs, AboutCompanyAboutPage


def home(req):
    info_block = {
        'about': AboutCompany.objects.first(),
        'docs': AboutDocs.objects.first(),
        'requisites': AboutRequisites.objects.first(),
        'contacts': AboutContacts.objects.first()
    }
    context = {
        'info_block': info_block,
        'stuff': Stuff.objects.all(),
        'news': News.objects.order_by('-date', '-id')[:3],
        'projects': Project.objects.order_by('-id')[:3],
        'ginfo': GeneralInfo.objects.first(),
        'actions': Actions.objects.all(),
        'settings': MainPageSettings.objects.first()
    }
    return render(req, 'tengApp/home.html', context)


def business_group(req):
    context = {
        'teyla_group': group_list(TeylaGroup.objects.order_by('-order', 'id'), 3),
        'ginfo': GeneralInfo.objects.first(),
        'settings': BusinessPageSettings.objects.first()
    }
    return render(req, 'tengApp/business_group.html', context)


def about(req):
    context = {
        'about': AboutCompanyAboutPage.objects.first(),
        'docs': group_list(Document.objects.order_by('-order', 'id'), 3),
        'requisites': Requisites.objects.first(),
        'settings': AboutPageSettings.objects.first(),
        'contacts': AboutContact.objects.first()
    }
    return render(req, 'tengApp/about.html', context)


def project(req):
    projects = Project.objects.select_related('area').order_by('-order', 'id')
    areas = []
    for area in ProjectArea.objects.order_by('-order', 'id'):
        d = {'id': area.id,
             'name': area.name,
             'lat': area.latitude,
             'lng': area.longitude,
             'zoom': area.zoom,
             'projects': group_list(projects.filter(area=area), 3)
             }
        areas.append(d)
    context = {
        'areas': areas,
        'settings': ProjectPageSettings.objects.first()
    }
    return render(req, 'tengApp/project.html', context=context)


def news(req, page_id=None):
    if not page_id:
        page_id = 1
    news_pages = Paginator(News.objects.all(), NEWS_PER_PAGE)
    context = {
        'news': news_pages.page(page_id),
        'settings': Settings.objects.first()
    }
    return render(req, 'tengApp/news.html', context=context)


def media(req, path):
    file_name = os.path.join(settings.MEDIA_ROOT, path)
    _, file_ext = os.path.splitext(file_name)
    image_data = open(file_name, 'rb').read()

    mime_types = {
        'image/jpeg': ('.jpg', '.jpeg'),
        'image/png': ('.png',),
        'application/pdf': ('.pdf',),
        'text/plain': ('.txt',)
    }

    content_type = 'application/octet-stream'  # default: binary data
    for mime, ext in mime_types.items():
        if file_ext.lower() in ext:
            content_type = mime
            break

    content_type = 'application/octet-stream'  # для того чтобы скачивалось, а не открывалось в браузере
    return HttpResponse(image_data, content_type=content_type)


def simple_page(req, page_url=None):
    page = FlatPages.objects.filter(url=page_url).first()
    if not page:
        return HttpResponseNotFound('Not found')
    context = {'page': page}
    return render(req, 'tengApp/simple_page.html', context=context)
