# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-04-28 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyze', '0005_unitview_games'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyzeUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('games', models.PositiveIntegerField()),
                ('mean', models.FloatField()),
                ('first', models.PositiveIntegerField()),
                ('top', models.PositiveIntegerField()),
                ('losses', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='UnitView',
        ),
    ]
