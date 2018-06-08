from django import template
from django.db.models import Q
from wiki.models import Definition

register = template.Library()


@register.filter(name='get_definition')
def get_definition(value, term):
    try:
        definition = Definition.objects.get(Q(acronym=term) | Q(term__iexact=term))
    except Definition.DoesNotExist:
        definition = None
    return definition
