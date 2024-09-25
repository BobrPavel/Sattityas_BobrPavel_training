from django import template
from django.utils.http import urlencode

register = template.Library()

@register.simple_tag(takes_context=True)
def change_params(context, **kwards):
    query = context['request'].GET.dict()
    query.update(kwards)
    return urlencode(query)