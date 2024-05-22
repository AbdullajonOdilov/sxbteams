from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value):
    while '/' in value:
        value = value[1:]
    return value