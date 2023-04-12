from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request,db_id=None):
    return render(request, 'tree_menu/index.html', {'db_id':db_id})

class MenusView(TemplateView):
    template_name = "tree_menu/index.html"