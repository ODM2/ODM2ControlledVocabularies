from django import template

register = template.Library()


@register.filter
def get(h, key):
    return h[key]


@register.inclusion_tag('cvinterface/requests/form_fields_snippet.html')
def print_field(field):
    return {'field': field}
