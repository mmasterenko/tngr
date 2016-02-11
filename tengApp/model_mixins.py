# -*- coding: utf-8 -*-
from django.db import models
from django.utils import six
from django.utils.encoding import smart_text


class OrderFieldMixin(models.Model):
    class Meta:
        abstract = True
    help_text = u'значение этого поля влияет на порядок следования элементов ' \
                u'(чем меньше значение, тем ниже расположен элемент)'
    order = models.SmallIntegerField(u'порядок', null=True, blank=True, help_text=help_text, default=-1)


class SEOFieldsMixin(models.Model):
    class Meta:
        abstract = True

    title = models.CharField('<title>', max_length=100, null=True, blank=True)
    meta_desc = models.CharField('meta description', max_length=100, null=True, blank=True)
    meta_keywords = models.CharField('meta keywords', max_length=100, null=True, blank=True)


class SlugNullField(models.SlugField):
    description = "SlugField that stores NULL but returns '' "

    def to_python(self, value):

        if value is None:
            return ''
        if isinstance(value, six.string_types):
            return value
        return smart_text(value)

    def get_prep_value(self, value):  # catches value right before sending to db

        value = super(SlugNullField, self).get_prep_value(value)
        if value == '':
            # if Django tries to save an empty string, send the db None (NULL)
            return None
        else:
            # otherwise, just pass the value
            return self.to_python(value)
