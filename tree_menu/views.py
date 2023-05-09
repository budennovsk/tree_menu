from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request: object, db_id=None) -> render:
    """ Домашняя страница"""
    return render(request, 'tree_menu/index.html', {'db_id': db_id})


class MenusView(TemplateView):
    """ Отображение домашней страницы """
    template_name = "tree_menu/index.html"
