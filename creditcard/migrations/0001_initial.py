# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-25 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='-', max_length=50)),
                ('holder', models.CharField(default='-', max_length=50)),
                ('issuer', models.CharField(default='-', max_length=50)),
                ('card', models.CharField(default='-', max_length=50)),
                ('issuedate', models.DateField()),
                ('closedate', models.DateField()),
                ('line', models.IntegerField(default=0)),
                ('fee', models.IntegerField(default=0)),
                ('minspend', models.IntegerField(default=0)),
                ('bonus', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PointsUsed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('where', models.CharField(default='-', max_length=50)),
                ('what', models.CharField(default='-', max_length=50)),
                ('dollar_cost', models.IntegerField(default=0)),
                ('point_cost', models.IntegerField(default=0)),
                ('info', models.CharField(default='-', max_length=50)),
            ],
        ),
    ]
