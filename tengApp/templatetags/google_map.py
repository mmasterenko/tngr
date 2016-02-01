from django import template
from tengApp.models import Project
import json

register = template.Library()


@register.simple_tag(takes_context=True)
def get_markers(context):
    request = context['request']
    markers = [marker for marker in Project.objects.values('latitude', 'longitude')]
    return json.dumps(markers)
