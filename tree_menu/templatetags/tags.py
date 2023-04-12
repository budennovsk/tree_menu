from django import template

from tree_menu.models import Menu

register = template.Library()

@register.inclusion_tag('tree_menu/menu_render.html', takes_context=True)
def draw_menu(context, db_id):
    obj = Menu.objects.filter(children=db_id)
    return {'menu': obj, 'elements': db_id, 'content': context}
