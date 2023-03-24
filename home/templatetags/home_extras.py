from django import template

from django.template.defaultfilters import stringfilter

from django.utils.html import conditional_escape, mark_safe
register = template.Library()

@register.filter
def get_item(dictionary, key):
    if dictionary.get(key) == 'doors':
        return dictionary.get(key)

@register.simple_tag(takes_context=True)
def set_global_context(context, key, value):
    """
    Sets a value to the global template context, so it can
    be accessible across blocks.

    Note that the block where the global context variable is set must appear
    before the other blocks using the variable IN THE BASE TEMPLATE.  The order
    of the blocks in the extending template is not important. 

    Usage::
        {% extends 'base.html' %}

        {% block first %}
            {% set_global_context 'foo' 'bar' %}
        {% endblock %}

        {% block second %}
            {{ foo }}
        {% endblock %}
    """
    context.dicts[0][key] = value
    return ''

 
 

@register.filter(name='get_data')
def get_data(data, key, value):
    if data.get(key) == 'make':
        return data.get(value)
    else:
        return ''



    

@register.simple_tag
def setvar(val=None):
  return val

# An upper function that capitalizes word passed to it.
@register.filter(name='upper')
def upper(value):
  return value.upper()

# An upper function that capitalizes the first letter of the word passed to it.
@register.filter(name='modify_name')
def modify_name(value):
    return value.title()

# An upper function that sets returns a red color.
@register.filter(name='get_color')
def color(value):
    if value:
        return "#FF0000"

    


