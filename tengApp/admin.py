# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import About, Document, GeneralInfo, News, Project, Requisites, Stuff, TeylaGroup


admin.site.register(About)
admin.site.register(Document)
admin.site.register(GeneralInfo)
admin.site.register(News)
admin.site.register(Project)
admin.site.register(Requisites)
admin.site.register(Stuff)
admin.site.register(TeylaGroup)

admin.site.site_header = u'Интерфейс администратора'
admin.site.index_title = u'Управление'
admin.site.site_title = u'Тейла Инжиниринг'
