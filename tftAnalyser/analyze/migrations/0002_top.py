# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-04-25 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyze', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('summoner_id', models.CharField(max_length=64)),
                ('league_points', models.PositiveSmallIntegerField()),
                ('wins', models.PositiveIntegerField()),
                ('losses', models.PositiveIntegerField()),
            ],
        ),
    ]