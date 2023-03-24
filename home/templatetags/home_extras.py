import json
from django import template

from django.template.defaultfilters import stringfilter

from django.utils.html import conditional_escape, mark_safe
register = template.Library()

@register.filter
def get_item(dictionary, key):
    if dictionary.get(key) == 'doors':
        return dictionary.get(key)


 
 
 
@register.filter(name='jsonify')
def jsonify(data):
    if isinstance(data, dict):
        return data
    else:
        return json.loads(data)


@register.filter(name='get_data')
def get_data(data, key, value):
    if data.get(key) == 'make':
        return data.get(value)
    else:
        return ''



@register.filter(needs_autoescape=True)

@stringfilter

def letter_count(value, letter, autoescape=True):

    if value == letter:
        # value = conditional_escape(value)
        result = (
            f'<span class="vehicle-result-title">{value} 2019</span>'
        )

        return mark_safe(result)

    

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

    


