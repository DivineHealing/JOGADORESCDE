from django import template

register = template.Library()

@register.filter
def get_attr(obj, attr_name):
    return getattr(obj, attr_name, '')

@register.filter
def concat(value, arg):
    return f"{value}{arg}"