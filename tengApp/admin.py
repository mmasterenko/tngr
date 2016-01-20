# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import About, Document, GeneralInfo, News, Project, Requisites, Stuff, TeylaGroup


class ProjectAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("model_assets/project.css",)
        }
        js = ("http://cdn.ckeditor.com/4.5.3/basic/ckeditor.js", "model_assets/project.js")


class TeylaGroupAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("model_assets/project.css",)
        }
        js = ("http://cdn.ckeditor.com/4.5.3/basic/ckeditor.js", "model_assets/project.js")


admin.site.register(About)
admin.site.register(Document)
admin.site.register(GeneralInfo)
admin.site.register(News)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Requisites)
admin.site.register(Stuff)
admin.site.register(TeylaGroup, TeylaGroupAdmin)

admin.site.site_header = u'Интерфейс администратора'
admin.site.index_title = u'Управление'
admin.site.site_title = u'Тейла Инжиниринг'
