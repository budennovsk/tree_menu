# Generated by Django 4.2 on 2023-04-12 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tree_menu", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="menu", name="is_main",),
    ]