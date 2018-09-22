# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-22 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='x', max_length=10000)),
                ('color', models.CharField(default='x', max_length=10000)),
                ('experience', models.CharField(default='x', max_length=10000)),
                ('char_class', models.CharField(default='x', max_length=10000)),
                ('race', models.CharField(default='x', max_length=10000)),
                ('level', models.CharField(default='x', max_length=10000)),
                ('background', models.CharField(default='x', max_length=10000)),
                ('alignment', models.CharField(default='x', max_length=10000)),
                ('hp', models.CharField(default='x', max_length=10000)),
                ('hit_die', models.CharField(default='x', max_length=10000)),
                ('ac', models.CharField(default='x', max_length=10000)),
                ('speed', models.CharField(default='x', max_length=10000)),
                ('prof_bonus', models.CharField(default='x', max_length=10000)),
                ('passive_perception', models.CharField(default='x', max_length=10000)),
                ('str_ability', models.CharField(default='x', max_length=10000)),
                ('dex_ability', models.CharField(default='x', max_length=10000)),
                ('con_ability', models.CharField(default='x', max_length=10000)),
                ('int_ability', models.CharField(default='x', max_length=10000)),
                ('wis_ability', models.CharField(default='x', max_length=10000)),
                ('char_ability', models.CharField(default='x', max_length=10000)),
                ('saving_throw', models.CharField(default='x', max_length=10000)),
                ('proficiencies', models.CharField(default='x', max_length=10000)),
                ('armor', models.CharField(default='x', max_length=10000)),
                ('weapon', models.CharField(default='x', max_length=10000)),
                ('spells', models.CharField(default='x', max_length=10000)),
                ('cantrip', models.CharField(default='x', max_length=100000)),
                ('level_1', models.CharField(default='x', max_length=100000)),
                ('level_2', models.CharField(default='x', max_length=100000)),
                ('level_3', models.CharField(default='x', max_length=100000)),
                ('level_4', models.CharField(default='x', max_length=100000)),
                ('level_5', models.CharField(default='x', max_length=100000)),
                ('level_6', models.CharField(default='x', max_length=100000)),
                ('level_7', models.CharField(default='x', max_length=100000)),
                ('level_8', models.CharField(default='x', max_length=100000)),
                ('level_9', models.CharField(default='x', max_length=100000)),
                ('other', models.CharField(default='x', max_length=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='x', max_length=10000)),
                ('size', models.CharField(default='x', max_length=10000)),
                ('type', models.CharField(default='x', max_length=10000)),
                ('alignment', models.CharField(default='x', max_length=10000)),
                ('hp', models.CharField(default='x', max_length=10000)),
                ('ac', models.CharField(default='x', max_length=10000)),
                ('speed', models.CharField(default='x', max_length=10000)),
                ('str_ability', models.CharField(default='x', max_length=10000)),
                ('dex_ability', models.CharField(default='x', max_length=10000)),
                ('con_ability', models.CharField(default='x', max_length=10000)),
                ('int_ability', models.CharField(default='x', max_length=10000)),
                ('wis_ability', models.CharField(default='x', max_length=10000)),
                ('char_ability', models.CharField(default='x', max_length=10000)),
                ('challenge', models.CharField(default='x', max_length=10000)),
                ('xp', models.CharField(default='x', max_length=10000)),
                ('languages', models.CharField(default='x', max_length=10000)),
                ('saving_throw', models.CharField(default='x', max_length=10000)),
                ('skills', models.CharField(default='x', max_length=10000)),
                ('damage_vulnerabilities', models.CharField(default='x', max_length=10000)),
                ('damage_immunities', models.CharField(default='x', max_length=10000)),
                ('condition_immunities', models.CharField(default='x', max_length=10000)),
                ('senses', models.CharField(default='x', max_length=10000)),
                ('actions', models.CharField(default='x', max_length=10000)),
                ('weapon', models.CharField(default='x', max_length=10000)),
                ('spells', models.CharField(default='x', max_length=10000)),
                ('cantrip', models.CharField(default='x', max_length=100000)),
                ('level', models.CharField(default='x', max_length=100000)),
                ('description', models.CharField(default='x', max_length=1000000)),
                ('other', models.CharField(default='x', max_length=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='Spells',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spell', models.CharField(default='x', max_length=10000)),
                ('spell_type', models.CharField(default='x', max_length=10000)),
                ('level', models.CharField(default='x', max_length=10000)),
                ('casting_time', models.CharField(default='x', max_length=10000)),
                ('range', models.CharField(default='x', max_length=10000)),
                ('components', models.CharField(default='x', max_length=10000)),
                ('duration', models.CharField(default='x', max_length=10000)),
                ('description', models.CharField(default='x', max_length=100000)),
                ('whose_spell', models.CharField(default='x', max_length=10000)),
                ('page', models.CharField(default='x', max_length=10000)),
            ],
        ),
    ]