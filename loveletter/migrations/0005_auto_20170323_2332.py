# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-23 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loveletter', '0004_game_gamestarted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='cards',
        ),
        migrations.AddField(
            model_name='player',
            name='card1',
            field=models.CharField(default='-1', max_length=1),
        ),
        migrations.AddField(
            model_name='player',
            name='card2',
            field=models.CharField(default='-1', max_length=1),
        ),
    ]