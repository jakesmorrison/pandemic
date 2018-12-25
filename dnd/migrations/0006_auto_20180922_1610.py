# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-22 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0005_auto_20180822_0308'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='characternew',
            name='ac',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='alignment',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='armor',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='background',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='cantrip',
            field=models.CharField(default='x', max_length=100000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='char_ability',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='char_class',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='color',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='con_ability',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='dex_ability',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='experience',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='hit_die',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='hp',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='int_ability',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='level',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='level_1',
            field=models.CharField(default='x', max_length=100000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='level_2',
            field=models.CharField(default='x', max_length=100000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='level_3',
            field=models.CharField(default='x', max_length=100000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='level_4',
            field=models.CharField(default='x', max_length=100000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='level_5',
            field=models.CharField(default='x', max_length=100000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='level_6',
            field=models.CharField(default='x', max_length=100000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='level_7',
            field=models.CharField(default='x', max_length=100000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='level_8',
            field=models.CharField(default='x', max_length=100000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='level_9',
            field=models.CharField(default='x', max_length=100000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='name',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='other',
            field=models.CharField(default='x', max_length=1000000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='passive_perception',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='prof_bonus',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='proficiencies',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='race',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='saving_throw',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='speed',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='spells',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='str_ability',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='weapon',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='characternew',
            name='wis_ability',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='spells',
            name='casting_time',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='spells',
            name='components',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='spells',
            name='duration',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='spells',
            name='level',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='spells',
            name='page',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='spells',
            name='range',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='spells',
            name='spell',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='spells',
            name='spell_type',
            field=models.CharField(default='x', max_length=10000),
        ),
        migrations.AlterField(
            model_name='spells',
            name='whose_spell',
            field=models.CharField(default='x', max_length=10000),
        ),
    ]
