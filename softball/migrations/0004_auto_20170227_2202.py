# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-27 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softball', '0003_auto_20170227_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='avg',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='stats',
            name='obp',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='stats',
            name='ops',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='stats',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stats',
            name='slg',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='stats',
            name='tb',
            field=models.IntegerField(default=0),
        ),
    ]
