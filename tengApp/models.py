# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.timezone import now
from .utils import SlugNullField

upload_path = 'images/original'
upload_file_path = 'files'

# модели для главной страницы


class GeneralInfo(models.Model):
    class Meta:
        verbose_name = u'общая информация'
        verbose_name_plural = u'общая информация'

    def __unicode__(self):
        return u'общая информация'

    phone = models.CharField(u'Телефон', max_length=20)
    email = models.EmailField(u'E-mail')
    address = models.CharField(u'Адрес', max_length=60)
    footerText = models.TextField(u'Текст в футере')

    #logo = models.ImageField(u'Логотип', upload_to=upload_path, null=True, blank=True)
    #slogan_mainPage = models.CharField(u'Слоган на главной', max_length=150, null=True, blank=True)
    #slogan_groupPage = models.CharField(u'Слоган Т-Бизнесс групп', max_length=150, null=True, blank=True)


class Project(models.Model):
    class Meta:
        verbose_name = u'проект'
        verbose_name_plural = u'проекты'

    def __unicode__(self):
        return self.name

    name = models.CharField(u'Название', max_length=100)
    company = models.CharField(u'Компания', max_length=100)
    desc = models.TextField(u'Описание')
    image = models.ImageField(u'Картинка', upload_to=upload_path)
    latitude = models.CharField(u'Широта', max_length=20, null=True, blank=True)
    longitude = models.CharField(u'Долгота', max_length=20, null=True, blank=True)


class About(models.Model):
    class Meta:
        verbose_name = u'информационный блок'
        verbose_name_plural = verbose_name

    CODE_CHOICE = (
        ('about', u'о компании'),
        ('docs', u'документы'),
        ('requisites', u'реквизиты'),
        ('contacts', u'контакты'),
    )

    def __unicode__(self):
        return self.get_code_display()

    name = models.CharField(u'Заголовок', max_length=100)
    desc = models.TextField(u'Текст')
    image = models.ImageField(u'Картинка', upload_to=upload_path, null=True, blank=True)
    code = models.CharField(max_length=15, choices=CODE_CHOICE, null=True)  # hidden in admin interface


class Stuff(models.Model):
    class Meta:
        verbose_name = u'наша команда'
        verbose_name_plural = verbose_name

    @property
    def full_name(self):
        return '%s %s' % (self.name, self.surname)

    def __unicode__(self):
        return self.full_name

    name = models.CharField(u'Имя', max_length=50)
    surname = models.CharField(u'Фамилия', max_length=50)
    position = models.CharField(u'Должность', max_length=50)
    quote = models.TextField(u'Цитата')
    photo = models.ImageField(u'Фото', upload_to=upload_path)


class News(models.Model):
    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'новости'

    def __unicode__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('news', args=[self.id])

    header = models.CharField(u'Заголовок', max_length=80)
    text = models.TextField(u'Текст')
    date = models.DateField(u'Дата', default=now)
    uri_help_text = u'URI под которым будет доступна новость. например: /udivitelnaya-novost/'
    url = SlugNullField(u'URI', help_text=uri_help_text, null=True, blank=True, unique=True, max_length=90, default=None)


class TeylaGroup(models.Model):
    class Meta:
        verbose_name = u'группа компаний'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    @property
    def link_plain(self):
        dlmtr = 'http://'  # dlmtr stands for delimiter
        if self.link.startswith(dlmtr):
            return self.link.split(dlmtr)[1]

    name = models.CharField(u'Название', max_length=100)
    link = models.URLField(u'Ссылка')
    desc = models.TextField(u'Описание')
    image = models.ImageField(u'Картинка', upload_to=upload_path)


class Document(models.Model):
    class Meta:
        verbose_name = u'документ'
        verbose_name_plural = u'документы'

    def __unicode__(self):
        return self.name

    name = models.CharField(u'Название', max_length=100)
    img = models.ImageField(u'Фото', upload_to=upload_path)


class Requisites(models.Model):
    class Meta:
        verbose_name = u'реквизиты'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'реквизиты'

    header = models.CharField(u'Заголовок', max_length=100)
    text = models.TextField(u'Текст')
    pdf = models.FileField(u'.pdf', upload_to=upload_file_path)
    doc = models.FileField(u'.doc', upload_to=upload_file_path)
    txt = models.FileField(u'.txt', upload_to=upload_file_path)

