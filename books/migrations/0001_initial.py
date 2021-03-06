# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-26 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100, unique=True)),
                ('Lookup', models.CharField(default='x', max_length=100)),
                ('Author', models.CharField(default='x', max_length=100)),
                ('Type', models.CharField(default='x', max_length=100)),
                ('Genre', models.CharField(default='x', max_length=100)),
                ('Date_Start', models.DateField()),
                ('Date_Finish', models.DateField()),
                ('Word_Count', models.IntegerField()),
                ('Unique_Words', models.IntegerField()),
                ('Vocab_Density', models.FloatField()),
                ('Word_List', models.TextField(null=True)),
            ],
        ),
    ]
