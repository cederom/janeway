# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-06-16 12:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    def forwards_func(apps, schema_editor):
        Role = apps.get_model("core", "Role")
        new_role = Role.objects.create(
            name='Reader',
            slug='reader',
        )

    def reverse_func(apps, schema_editor):
        Role = apps.get_model("core", "Role")
        new_role = Role.objects.filter(
            name='Reader',
            slug='reader',
        ).delete()

    dependencies = [
        ('core', '0070_auto_20220506_1652'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]