from django import template

register = template.Library()

@register.simple_tag
def compare_values(value1, value2):
    return value1 == value2