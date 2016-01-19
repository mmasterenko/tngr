from django.db import models
from django.utils import six
from django.utils.encoding import smart_text


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
