from django.contrib import admin

from tree_menu.models import *


# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    """ Настройка админки"""
    list_display = ('name', 'parent', 'id')


admin.site.register(Menu, MenuAdmin)
