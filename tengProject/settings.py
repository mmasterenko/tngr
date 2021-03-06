# -*- coding: utf-8 -*-

"""
Django settings for tengProject project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w&p-_yl(3hxolrf9p*@hu)o2^p!7q))bz(oh5xr=&9quxg_)@v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'admin_shortcuts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tengApp'
)

ADMIN_SHORTCUTS = [
    {
        'shortcuts': [
            {
                'url_name': 'admin:tengApp_generalinfo_changelist',
                'url_extra': '1',
                'title': u'Общая информация',
                'class': 'home'
            },
            {
                'url_name': 'admin:tengApp_flatpages_changelist',
                'title': u'Простые страницы',
                'class': 'file2'
            },
            {
                'url_name': 'admin:tengApp_news_changelist',
                'title': u'Новости',
                'class': 'date'
            },
        ]
    },
    {
        'title': u'Главная Страница',
        'shortcuts': [
            {
                'url_name': 'admin:tengApp_mainpagesettings_changelist',
                'url_extra': '1',
                'title': u'Настройки',
                'class': 'config'
            },
            {
                'url_name': 'admin:tengApp_actions_changelist',
                'title': u'Баннеры',
                'class': 'picture'
            },
            {
                'url_name': 'admin:tengApp_stuff_changelist',
                'title': u'Наша команда',
                'class': 'user'
            },
            {
                'url_name': 'admin:tengApp_aboutcompany_changelist',
                'title': u'О компании',
                'class': 'note',
                'url_extra': '1'
            },
            {
                'url_name': 'admin:tengApp_aboutdocs_changelist',
                'title': u'Документы',
                'class': 'certificate',
                'url_extra': '1'
            },
            {
                'url_name': 'admin:tengApp_aboutrequisites_changelist',
                'title': u'Реквизиты',
                'class': 'card',
                'url_extra': '1'
            },
            {
                'url_name': 'admin:tengApp_aboutcontacts_changelist',
                'title': u'Контакты',
                'class': 'phone',
                'url_extra': '1'
            },
        ]
    },
    {
        'title': u'Страница "Проекты"',
        'shortcuts': [
            {
                'url_name': 'admin:tengApp_projectpagesettings_changelist',
                'url_extra': '1',
                'title': u'Настройки',
                'class': 'config'
            },
            {
                'url_name': 'admin:tengApp_projectarea_changelist',
                'title': u'Регионы',
                'class': 'pin'
            },
            {
                'url_name': 'admin:tengApp_project_changelist',
                'title': u'Проекты',
                'class': 'flag'
            },
        ]
    },
    {
        'title': u'Страница "О компании"',
        'shortcuts': [
            {
                'url_name': 'admin:tengApp_aboutpagesettings_changelist',
                'url_extra': '1',
                'title': u'Настройки',
                'class': 'config'
            },
            {
                'url_name': 'admin:tengApp_aboutcompanyaboutpage_changelist',
                'title': u'О компании',
                'class': 'note',
                'url_extra': '1',
            },
            {
                'url_name': 'admin:tengApp_document_changelist',
                'title': u'Документы',
                'class': 'certificate'
            },
            {
                'url_name': 'admin:tengApp_requisites_changelist',
                'url_extra': '1',
                'title': u'Реквизиты',
                'class': 'card'
            },
            {
                'url_name': 'admin:tengApp_aboutcontact_changelist',
                'url_extra': '1',
                'title': u'Контакты',
                'class': 'phone'
            },
        ]
    },
    {
        'title': u'Страница "Т-Бизнесс группа"',
        'shortcuts': [
            {
                'url_name': 'admin:tengApp_businesspagesettings_changelist',
                'url_extra': '1',
                'title': u'Настройки',
                'class': 'config'
            },
            {
                'url_name': 'admin:tengApp_teylagroup_changelist',
                'title': u'Группа компаний Teyla',
                'class': 'tag'
            }
        ]
    },
]

ADMIN_SHORTCUTS_SETTINGS = {
    'hide_app_list': True,
    'open_new_window': False,
}

# todo:
# ADMIN_SHORTCUTS_CLASS_MAPPINGS
# https://github.com/alesdotio/django-admin-shortcuts/blob/master/admin_shortcuts/templatetags/admin_shortcuts_tags.py

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'tengProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'tengApp.context_processors.general_info'
            ],
        },
    },
]

WSGI_APPLICATION = 'tengProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# # # # # # # # # #
# heroku settings #
# # # # # # # # # #

import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static_dir_dev'),
)

# *** import development settings if exists ***

try:
    from settings_dev import *
except ImportError:
    pass


