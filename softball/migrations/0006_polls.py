# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-08 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('softball', '0005_auto_20170227_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='x', max_length=1000)),
                ('poss', picklefield.fields.PickledObjectField(default={}, editable=False)),
            ],
        ),
    ]
