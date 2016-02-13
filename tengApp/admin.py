# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *


class AboutAdmin(admin.ModelAdmin):
    actions = None
    fields = ['name', 'desc', 'image']


class ProjectAreaAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("model_assets/project.css",)
        }
        js = (
              "model_assets/projectarea_map.js",
              "model_assets/projectarea.js",
              )
    list_display = ('name', 'latitude', 'longitude', 'zoom', 'order')
    list_display_links = ('name',)
    list_editable = ('order',)
    ordering = ('-order', 'id')
    fieldsets = [
        (None, {
            'fields': ('name',),
            'classes': ('wide',)
        }),
        (u'Настройки карты', {
            'fields': ('zoom', ('latitude', 'longitude')),
            'description': u'С помощью карты задайте центральную точку и масштаб для данного региона'
        })
    ]


class ProjectAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("model_assets/project.css",)
        }
        js = ("http://cdn.ckeditor.com/4.5.3/basic/ckeditor.js",
              "model_assets/project_map.js",
              "model_assets/project.js",
              )
    list_display = ('name', 'company', 'area', 'order')
    list_display_links = ('name',)
    list_filter = ('area',)
    list_editable = ('order',)
    ordering = ('-order', 'id')
    fieldsets = [
        (None, {
            'fields': ('area', 'name', 'company', 'image', 'desc'),
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
    list_display = ('name', 'link', 'order')
    list_editable = ('order',)
    ordering = ('-order', 'id')
    exclude = ('order',)


class RequisitesAdmin(admin.ModelAdmin):
    actions = None


class ActionsAdmin(admin.ModelAdmin):
    list_display = ('header', 'is_hide_header', 'is_hide_text', 'order')
    list_editable = ('order',)
    ordering = ('-order', 'id')
    exclude = ('order',)


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
    fieldsets = [
        (None, {
            'fields': ('header', 'date', 'text'),
            'classes': ('wide',)
        }),
    ]
    # prepopulated_fields = {'url': ('header',)}
    list_display = ('header', 'url', 'date')
    date_hierarchy = 'date'


class FlatPagesAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("model_assets/ckeditor.css",)
        }
        js = ("http://cdn.ckeditor.com/4.5.7/full/ckeditor.js", "model_assets/ckeditor.js")
    list_display = ('header', 'menu', 'submenu', 'url', 'order')
    list_display_links = ('header',)
    list_filter = ('menu',)
    list_editable = ('order',)
    ordering = ('-order', 'id')
    fieldsets = [
        (None, {
            'fields': ('menu', 'submenu', 'header', 'url', 'order', 'text'),
            'classes': ('wide',)
        }),
        (u'SEO настройки', {
            'fields': ('title', 'meta_desc', 'meta_keywords'),
            'classes': ('wide', 'collapse'),
        })
    ]
    prepopulated_fields = {'url': ('header',)}


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    ordering = ('-order', 'id')
    exclude = ('order',)


class MainPageSettingsAdmin(admin.ModelAdmin):
    actions = None
    fieldsets = [
        (None, {
            'fields': ('slogan',),
            'classes': ('wide',)
        }),
        (u'SEO настройки', {
            'fields': ('title', 'meta_desc', 'meta_keywords'),
            'classes': ('wide', 'collapse'),
        })
    ]


class ProjectPageSettingsAdmin(admin.ModelAdmin):
    actions = None
    fieldsets = [
        (u'SEO настройки', {
            'fields': ('title', 'meta_desc', 'meta_keywords'),
            'classes': ('wide',),
        })
    ]


class AboutPageSettingsAdmin(admin.ModelAdmin):
    actions = None
    fieldsets = [
        (None, {
            'fields': ('header',),
            'classes': ('wide',)
        }),
        (u'SEO настройки', {
            'fields': ('title', 'meta_desc', 'meta_keywords'),
            'classes': ('wide', 'collapse'),
        })
    ]


class BusinessPageSettingsAdmin(admin.ModelAdmin):
    actions = None
    fieldsets = [
        (None, {
            'fields': ('header', 'slogan'),
            'classes': ('wide',)
        }),
        (u'SEO настройки', {
            'fields': ('title', 'meta_desc', 'meta_keywords'),
            'classes': ('wide', 'collapse'),
        })
    ]


class GeneralInfoAdmin(admin.ModelAdmin):
    actions = None
    exclude = ('slogan_mainPage', 'slogan_groupPage')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'position', 'quote')
    ordering = ('id',)


class AboutContactAdmin(admin.ModelAdmin):
    actions = None


admin.site.register(GeneralInfo, GeneralInfoAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectArea, ProjectAreaAdmin)
admin.site.register(Requisites, RequisitesAdmin)
admin.site.register(Stuff, StaffAdmin)
admin.site.register(TeylaGroup, TeylaGroupAdmin)
admin.site.register(Actions, ActionsAdmin)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(FlatPages, FlatPagesAdmin)
admin.site.register(MainPageSettings, MainPageSettingsAdmin)
admin.site.register(ProjectPageSettings, ProjectPageSettingsAdmin)
admin.site.register(AboutPageSettings, AboutPageSettingsAdmin)
admin.site.register(BusinessPageSettings, BusinessPageSettingsAdmin)
admin.site.register(AboutContact, AboutContactAdmin)

admin.site.site_header = u'Тейла Инжиниринг / Интерфейс администратора'
admin.site.index_title = u'Управление'
admin.site.site_title = u'Тейла Инжиниринг'
