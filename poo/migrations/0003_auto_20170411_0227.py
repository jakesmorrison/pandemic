# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-11 02:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poo', '0002_poo_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poo',
            old_name='location',
            new_name='loc',
        ),
    ]
