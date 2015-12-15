from django import template
from lab3.models import Recall

register = template.Library()


@register.filter
def get_recalls(value):
    """Removes all values of arg from the given string"""
    return Recall.objects.filter(product_id=value)
