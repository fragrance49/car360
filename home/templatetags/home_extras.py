from django import template

from django.template.defaultfilters import stringfilter

from django.utils.html import conditional_escape, mark_safe
register = template.Library()

@register.filter
def get_item(dictionary, key):
    if dictionary.get(key) == 'doors':
        return dictionary.get(key)


@register.filter(needs_autoescape=True)

@stringfilter

def letter_count(value, letter, autoescape=True):

    if value == letter:
        # value = conditional_escape(value)
        result = (
            f'<span class="vehicle-result-title">{value} 2019</span>'
        )

        return mark_safe(result)

@register.filter(name='get_citem')
def get_citem(dictionary,key):
    if dictionary.get(key) == 'doors':
        return dictionary
    

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

    

# A function that sets returns the number of contacts.
@register.simple_tag(name='my_contacts')
def my_contacts():
    return Contact.objects.all().count()

# A function that sets returns the current date.
@register.simple_tag(name='current_date')
def current_date(format):
    return datetime.datetime.now().strftime(format)
