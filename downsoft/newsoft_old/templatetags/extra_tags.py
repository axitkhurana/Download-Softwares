from django import template
import re
register = template.Library()

@register.filter
def hash(h,key):
    if key in h:
        return h[key]
    else:
        return None

@register.filter
def listify(value):
	return re.split('\W+',value)
