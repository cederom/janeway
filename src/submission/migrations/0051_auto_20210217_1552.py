# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-17 15:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0050_support_ordered_keywords'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sectiontranslation',
            old_name='name',
            new_name='hvad_name',
        ),
        migrations.RenameField(
            model_name='sectiontranslation',
            old_name='plural',
            new_name='hvad_plural',
        ),
    ]
