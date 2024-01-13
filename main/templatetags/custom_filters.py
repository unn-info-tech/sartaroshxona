# In your_app/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='sum_attribute')
def sum_attribute(queryset, attribute):
    return sum(getattr(obj, attribute) for obj in queryset)
