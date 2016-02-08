# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import About, Document, GeneralInfo, News, Project, Requisites, Stuff, TeylaGroup, Actions


class AboutAdmin(admin.ModelAdmin):
    actions = None
    fields = ['name', 'desc', 'image']


class ProjectAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("model_assets/project.css",)
        }
        js = ("http://cdn.ckeditor.com/4.5.3/basic/ckeditor.js",
              "model_assets/project_map.js",
              "model_assets/project.js",
              )

    fieldsets = [
        (None, {
            'fields': ('name', 'company', 'image', 'desc'),
        }),
        (u'Координаты проекта', {
            'fields': (('latitude', 'longitude'),),
        })
    ]


class TeylaGroupAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("model_assets/teylagroup.css",)
        }
        js = ("http://cdn.ckeditor.com/4.5.3/basic/ckeditor.js", "model_assets/teylagroup.js")


class RequisitesAdmin(admin.ModelAdmin):
    actions = None


#class ActionsAdmin(admin.ModelAdmin):
#    actions = None


admin.site.register(About, AboutAdmin)
admin.site.register(Document)
admin.site.register(GeneralInfo)
admin.site.register(News)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Requisites, RequisitesAdmin)
admin.site.register(Stuff)
admin.site.register(TeylaGroup, TeylaGroupAdmin)
admin.site.register(Actions)

admin.site.site_header = u'Тейла Инжиниринг / Интерфейс администратора'
admin.site.index_title = u'Управление'
admin.site.site_title = u'Тейла Инжиниринг'
