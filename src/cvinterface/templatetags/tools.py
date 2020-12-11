from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag(name='detail_url', takes_context=True)
def get_detail_url(context, instance):
    return reverse(context['detail_url_name'], args=(instance.term,))


@register.filter
def get(h, key):
    return h[key]


@register.inclusion_tag('cvinterface/requests/form_fields_snippet.html')
def print_field(field):
    return {'field': field}
