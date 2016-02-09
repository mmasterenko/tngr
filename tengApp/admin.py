# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import About, Document, GeneralInfo, News, Project, Requisites, \
    Stuff, TeylaGroup, Actions, Settings, FlatPages


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


class SettingsAdmin(admin.ModelAdmin):
    actions = None
    fieldsets = [
        (u'Главная страница', {
            'fields': ('indexPage_title', 'indexPage_meta_desc', 'indexPage_meta_keywords'),
            'classes': ('collapse', 'wide')
        }),
        (u'Страница "Проекты"', {
            'fields': ('projectPage_title', 'projectPage_meta_desc', 'projectPage_meta_keywords'),
            'classes': ('collapse', 'wide')
        }),
        (u'Страница "О компании"', {
            'fields': ('aboutPage_header', 'aboutPage_title', 'aboutPage_meta_desc', 'aboutPage_meta_keywords'),
            'classes': ('collapse', 'wide')
        }),
        (u'Страница "Т-бизнесс группа"', {
            'fields': ('businessPage_header', 'businessPage_title', 'businessPage_meta_desc', 'businessPage_meta_keywords'),
            'classes': ('collapse', 'wide')
        }),
        (u'Страница "Новости"', {
            'fields': ('newsPage_header', 'newsPage_title', 'newsPage_meta_desc', 'newsPage_meta_keywords'),
            'classes': ('collapse', 'wide')
        }),
    ]


class NewsAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("model_assets/ckeditor.css",)
        }
        js = ("http://cdn.ckeditor.com/4.5.7/standard/ckeditor.js", "model_assets/ckeditor.js")
    fields = ('header', 'date', 'url', 'text')
    prepopulated_fields = {'url': ('header',)}


class FlatPagesAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("model_assets/ckeditor.css",)
        }
        js = ("http://cdn.ckeditor.com/4.5.7/full/ckeditor.js", "model_assets/ckeditor.js")
    list_display = ('header', 'menu', 'submenu', 'url')
    list_filter = ('menu',)
    fieldsets = [
        (None, {
            'fields': ('menu', 'submenu', 'header', 'url', 'text'),
            'classes': ('wide',)
        }),
        (u'SEO настройки', {
            'fields': ('title', 'meta_desc', 'meta_keywords'),
            'classes': ('wide', 'collapse'),
        })
    ]
    prepopulated_fields = {'url': ('header',)}


admin.site.register(About, AboutAdmin)
admin.site.register(Document)
admin.site.register(GeneralInfo)
admin.site.register(News, NewsAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Requisites, RequisitesAdmin)
admin.site.register(Stuff)
admin.site.register(TeylaGroup, TeylaGroupAdmin)
admin.site.register(Actions)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(FlatPages, FlatPagesAdmin)

admin.site.site_header = u'Тейла Инжиниринг / Интерфейс администратора'
admin.site.index_title = u'Управление'
admin.site.site_title = u'Тейла Инжиниринг'
