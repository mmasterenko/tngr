from django import template
from tengApp.models import Project
import json

register = template.Library()


@register.simple_tag
def get_markers():
    markers = list(Project.objects.values('latitude', 'longitude', 'name', 'company', 'desc', 'image'))
    return json.dumps(markers)
