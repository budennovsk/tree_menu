from django import template

from tree_menu.models import Menu

register = template.Library()


@register.inclusion_tag('tree_menu/menu_render.html', takes_context=True)
def draw_menu(context: object, db_id: str) -> object:
    """Расширение шаблона, отображение рекурсии"""
    obj = Menu.objects.filter(children=db_id)
    return {'menu': obj, 'elements': db_id, 'content': context}
