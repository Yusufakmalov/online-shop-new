from django import template
from ..models import Category


register = template.Library()

@register.simple_tag
def get_categories_by_id(category_id):
    try:
        return Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return None