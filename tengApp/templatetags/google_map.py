from django import template
from tengApp.models import Project
import json

register = template.Library()


@register.simple_tag(takes_context=True)
def get_markers(context):
    request = context['request']
    markers = list(Project.objects.values('latitude', 'longitude', 'name', 'company', 'desc', 'image'))
    return json.dumps(markers)
