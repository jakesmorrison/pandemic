# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-24 01:07
from __future__ import unicode_literals

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('loveletter', '0005_auto_20170323_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='cardsPlayed',
            field=picklefield.fields.PickledObjectField(default={}, editable=False),
        ),
        migrations.AlterField(
            model_name='game',
            name='gameDeck',
            field=picklefield.fields.PickledObjectField(default={}, editable=False),
        ),
    ]