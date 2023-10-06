from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag('menu/menu.html')
def draw_menu(menu_name, current_url):
    try:
        menu = Category.objects.get(title=menu_name)
        categories = menu.children.all().order_by('id')
    except Category.DoesNotExist:
        categories = []
    
    return {'categories': categories, 'current_url': current_url}