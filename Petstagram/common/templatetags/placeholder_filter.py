from django import template

register = template.Library()


@register.filter
def placeholder(value, placeholder_text):
    value.field.widget.attrs['placeholder'] = placeholder_text
    return value
